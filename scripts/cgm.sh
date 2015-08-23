#!/bin/bash
python scripts/cgm.py $@

module load lammps-31Jan14
lmp_linux < cgm_temp.in

python /home/maldonis/model_analysis/scripts/model.py temp.dat -o xyz > output.xyz

echo
echo "WROTE FINAL XYZ FILE TO output.xyz"
echo "Additional files written include: log.lammps, cgm_temp.in, temp.dat and they were automatically deleted!"
echo
rm log.lammps
rm cgm_temp.in
rm temp.dat
