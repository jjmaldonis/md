#!/bin/bash
python scripts/cgm.py $@

module load lammps-31Jan14
lmp_linux < cgm_temp.in

python /home/maldonis/model_analysis/scripts/model.py temp.dat -o xyz > post_cgm.xyz

echo
echo "WROTE FINAL XYZ FILE TO post_cgm.xyz"
echo "Additional files written include: lmp_emin_exp.restart, log.lammps, cgm_temp.in, temp.dat"
echo
