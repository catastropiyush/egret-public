# Egret Neural Network Potentials

<p align="center">
<img src="docs/visual_abstract.png" alt="Visual Abstract" width="650"/>
</p>

This repository contains the **Egret** family of neural network potentials, developed by Rowan using the [MACE](https://github.com/ACEsuit/mace) architecture. You can use the pretrained model weights locally or run predictions directly via the [Rowan web platform](https://labs.rowansci.com/).

For more information on the models, see [the preprint](https://rowansci.com/publications/egret-1-pretrained-neural-network-potentials).

For questions or issues, please open a GitHub issue or contact the Rowan team at contact@rowansci.com.

## Egret Model Suite

We provide three general-purpose models, released under the MIT license:

- **Egret-1** — optimized for bioorganic molecules; a strong general-purpose model  
- **Egret-1e** — enhanced with main-group chemistry data; excels at thermochemistry  
- **Egret-1t** — trained on transition states; ideal for modeling chemical reactivity  

## Example: Using Egret-1 with ASE
Egret-1 is compatible with the [Atomic Simulation Environment](https://wiki.fysik.dtu.dk/ase/) interface. The following is an example using the `mace_off` calculator from the [`mace-torch`](https://github.com/ACEsuit/mace) package:

### Energy and Force Prediction

```python
import ase.io
from ase.calculators.calculator import all_changes

from mace.calculators import mace_off

atoms = read("<path_to_molecule_file>")

calculator = mace_off(model="<path_to_model/EGRET_1.model>", default_dtype="float64")

calculator.calculate(atoms, ["<ASE_task_1>", "<ASE_task_2>"], all_changes)

print(calculator.results)
```

### Extracting Node Features

To get the full equivariant descriptors from the model (of shape `[L,1920]` where `L` is the number of atoms):

```python
equivariant_descriptor = calculator.models[0](
    calculator._atoms_to_batch(atoms).to_dict(),
)["node_feats"]

```

To extract the invariant descriptors (of shape `[Lx384]` where `L` is the number of atoms):

```python
invariant_descriptor = torch.cat([
    full_descriptor[:, :192],
    full_descriptor[:, -192:],
], dim=1)
```

Invariant features are recommend for scalar property prediction tasks that do not change with rotation like energy or HOMO-LUMO gap. Equivariant features are recommended for tasks that do depend on rotation like dipole moments or forces.

**Descriptor Pooling**

When pooling features over atoms to obtain a single vector as a molecular descriptor, we recommend a sum for `invariant_descriptor.sum(dim=0)` extensive property prediction which scale with system size like energy or heat capacity. Mean pooling `invariant_descriptor.mean(dim=0)` is recommended for intensive properties that do not scale with system size like refractive index or melting point.


## Local Usage
Install the required packages using 
```
conda env create -f environment.yml
conda activate egret-env      
```

To run the example script, run 
```
python example.py
```

These models can run on either CPU or GPU. 

