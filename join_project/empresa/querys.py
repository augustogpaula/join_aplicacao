# -- 1.A
# SELECT nome, nome_cargo AS cargo FROM empresa_funcionarios AS P
# JOIN empresa_cargos AS C ON P.cargo_id = C.id
# ORDER BY admissao
#
# -- 1.B
# SELECT nome, nome_cargo AS cargo FROM empresa_funcionarios AS P
# JOIN empresa_cargos AS C ON P.cargo_id = C.id
# ORDER BY admissao LIMIT 1
#
# -- 1.C
# SELECT nome_cargo AS cargo, count(P.id) as qtd_funcionarios
# FROM empresa_funcionarios AS P
# JOIN empresa_cargos AS C ON P.cargo_id = C.id GROUP BY C.id