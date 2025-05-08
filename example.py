import ase.io
import torch
from ase.calculators.calculator import all_changes
from mace.calculators import mace_off


atoms = ase.io.read("static/aspirin.xyz", format="xyz")
calculator = mace_off(model="compiled_models/EGRET_1.model", default_dtype="float64")

#to predict energies and forces
calculator.calculate(atoms, ["energy", "forces"], all_changes)
print(calculator.results)

#to obtain node features to use as a molecule descriptor
full_descriptor = calculator.models[0](calculator._atoms_to_batch(atoms).to_dict())["node_feats"]
print(f'{full_descriptor.shape=}')

#to extract only the inviariant features
invariant_descriptor = torch.cat([
    full_descriptor[:, :192],
    full_descriptor[:, -192:],
], dim=1)
print(f'{invariant_descriptor.shape=}')
