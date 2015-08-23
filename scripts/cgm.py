from model import Model
import sys

def main():
    modelfile = sys.argv[1]
    m = Model(modelfile)
    extension = modelfile.split('.')[-1]
    m.write('temp.dat')

    of = open("cgm_temp.in", 'w')
    of.write("""units		metal
boundary	p p p
atom_style	atomic

read_data temp.dat

pair_style	eam/alloy
pair_coeff	* * potentials/ZrCuAl2011.eam.alloy Zr Cu Al

thermo_style	custom step etotal fmax fnorm
thermo		1

minimize	1.0e-6 0 1000 10000
write_data  output.dat""")
    of.close()

if __name__== '__main__':
    main()
