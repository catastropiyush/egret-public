import ase.io
from ase.calculators.calculator import all_changes

from mace.calculators import mace_off

atoms = ase.io.read("static/aspirin.xyz", format="xyz")

calculator = mace_off(model="compiled_models/EGRET_1.model", default_dtype="float32")

calculator.calculate(atoms, ["energy", "forces"], all_changes)

print(calculator.results)