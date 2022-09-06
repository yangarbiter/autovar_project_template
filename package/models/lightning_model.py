import torch
from pytorch_lightning import LightningModule
import numpy as np
from tqdm import tqdm
from torch.optim.lr_scheduler import StepLR

from .torch_utils import get_optimizer, get_loss
from . import archs


class TorchLightningModel(LightningModule):

    def __init__(self, n_features, n_classes, epochs, arch, loss_name='ce',
        learning_rate=1e-4, momentum=0.0, optimizer='sgd', train_type=None):

        print(f'[TorchLightningModel] lr: {learning_rate}, opt: {optimizer}, loss: {loss_name}, '
              f'momentum: {momentum}, train_type: {train_type}')

        super().__init__()
        self.n_features = n_features
        self.n_classes = n_classes
        self.learning_rate = learning_rate
        self.loss_name = loss_name
        self.optimizer = optimizer
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.epochs = epochs
        self.arch = arch

        arch_fn = getattr(archs, self.arch)
        arch_params = dict(n_features=n_features, n_classes=n_classes)
        self.model = arch_fn(**arch_params)

        self.loss_fn = get_loss(self.loss_name, reduction="none")

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_nb):
        x, y = batch
        logits = self(x)
        loss = self.loss_fn(logits, y)
        loss = loss.mean()

        self.log('trn_loss', loss, on_step=True, on_epoch=True, prog_bar=False, logger=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = self.loss_fn(logits, y).mean()
        self.log('tst_loss', loss, on_step=True, on_epoch=True, prog_bar=True)

    def predict_step(self, batch, batch_idx: int , dataloader_idx: int = None):
        return self(batch[0])

    def configure_optimizers(self):
        opt = get_optimizer(self.model, self.optimizer, self.learning_rate, self.momentum)
        scheduler = StepLR(opt, step_size=25, gamma=0.1)
        return [opt], [scheduler]
            
    def predict_ds(self, ds, batch_size=32, num_workers=12, device='cuda'):
        self.model.eval()
        loader = torch.utils.data.DataLoader(
            ds, batch_size=batch_size, shuffle=False, num_workers=num_workers)
        ret = []
        for x in tqdm(loader, desc="[predict_ds]"):
            with torch.no_grad():
                pred = self.model(x[0].to(device)).cpu().numpy()
            ret.append(pred)
        del loader
        return np.concatenate(ret)
