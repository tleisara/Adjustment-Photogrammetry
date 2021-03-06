import numpy as np

def lstSqrtAffine( A, L ):
    N = np.matmul( np.transpose( A ), A )
    U = np.matmul( np.transpose( A ), L )
    Xa = np.matmul( -1*np.linalg.inv( N ), U )
    V = np.matmul( A, Xa ) + L
    return ( Xa, V )


A_62 = np.array( [ [15088,       7561,       1,         0,           0,           0],
     [0,             0,           0,       15088,       7561,        1],
     [34,            7561,        1,       0,           0,           0],
     [0,             0,           0,       34,          7561,        1],
     [7561,          32,          1,       0,           0,           0],
     [0,             0,           0,       7561,        32,          1],
     [7560,	     15088,       1,       0,           0,           0],
     [0,             0,           0,       7560,       15088,        1],
     [15088,	     33,          1,       0,           0,           0],
     [0,             0,           0,       15088,       33,          1],
     [33,	     15088,        1,       0,           0,           0],
     [0,             0,           0,       33,          15088,       1],
     [33,	     33,          1,       0,           0,           0],
     [0,             0,           0,       33,          33,          1],
     [15088,	     15088,       1,       0,           0,           0],
     [0,             0,           0,       15088,       15088,       1] ] )

A_63 = np.array( [ [15088,       7560,       1,         0,           0,           0],
     [0,             0,           0,       15088,       7560,        1],
     [34,            7561,        1,       0,           0,           0],
     [0,             0,           0,       34,          7561,        1],
     [7561,          32,          1,       0,           0,           0],
     [0,             0,           0,       7561,        32,          1],
     [7560,	     15088,       1,       0,           0,           0],
     [0,             0,           0,       7560,       15088,        1],
     [15088,	     33,          1,       0,           0,           0],
     [0,             0,           0,       15088,       33,          1],
     [34,	     15088,       1,       0,           0,           0],
     [0,             0,           0,       34,          15088,       1],
     [33,	     33,          1,       0,           0,           0],
     [0,             0,           0,       33,          33,          1],
     [15088,	     15088,       1,       0,           0,           0],
     [0,             0,           0,       15088,       15088,       1] ] )




L = -1*np.array( [ [ 113.003 ],	
        [0.006],
        [-112.987], 
        [0.006],	
        [0.012],	
        [113.023],
        [0.012],	
        [-113.004],
        [113.007],
        [113.005],	
        [-112.989],	
        [-112.994],
        [-112.998],
        [113.006],
        [112.999],
        [-112.998] ] )



Xa_62, V_62 = lstSqrtAffine( A_62, L )
Xa_63, V_63 = lstSqrtAffine( A_63, L )

print( 'parameter of img 62', Xa_62, '\n',  'residal of img 62', V_62 ,'\n')
print(  '\n', 'parameter of img 63', Xa_63, '\n',  'residal of img 63', V_63 ,'\n' ) 




























