# RAFAEL SADEWO AI SAKTI
# 235150301111029

import sympy as sp

# Definisi Variabel Simbolik
t, s = sp.symbols('t s')
V, I, w, T = sp.symbols('V I w T')  # Tegangan, Arus, Kecepatan Sudut, Torsi
R, L, Kt, Ke, J, B = sp.symbols('R L Kt Ke J B')  # Parameter Motor DC

# Persamaan Listrik Motor DC
V_eq = sp.Eq(V, R*I + L*sp.diff(I, t) + Ke*w)

# Persamaan Mekanik Motor DC
T_eq = sp.Eq(Kt*I, J*sp.diff(w, t) + B*w)

# Transformasi Laplace
I_s, W_s = sp.symbols('I_s W_s')
V_s = sp.symbols('V_s')

# Transformasi Laplace dari Persamaan Listrik
V_s_eq = sp.Eq(V_s, R*I_s + L*(s*I_s) + Ke*W_s)

# Transformasi Laplace dari Persamaan Mekanik
T_s_eq = sp.Eq(Kt*I_s, J*(s*W_s) + B*W_s)

# Fungsi Alih (Kecepatan Sudut terhadap Tegangan)
I_s_expr = sp.solve(V_s_eq, I_s)[0]
W_s_expr = sp.solve(T_s_eq.subs(I_s, I_s_expr), W_s)[0]
G_s = sp.simplify(W_s_expr / V_s)

# Output Hasil
print("Persamaan Listrik Motor DC:")
sp.pprint(V_eq)
print("\nPersamaan Mekanik Motor DC:")
sp.pprint(T_eq)
print("\nTransformasi Laplace Persamaan Listrik:")
sp.pprint(V_s_eq)
print("\nTransformasi Laplace Persamaan Mekanik:")
sp.pprint(T_s_eq)
print("\nFungsi Alih (W_s / V_s):")
sp.pprint(G_s)
