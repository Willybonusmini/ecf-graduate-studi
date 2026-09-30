#exercice 

#Si Arrive des clients.
#    vérifier la disponibilité des tables.
#    attibuer une table en fonction de la taille du groupe.

#sinon en cas d'une seule personne atribuir une place a table de 2 places.
#    Gérer une liste d'attente si aucune table n'est disponible.
#fin si 
print("restaurante geminiwilson")

groupes_clients = [6, 1, 4, 2, 5] 
liste_attente = []

tables_disponibles = {
    2: 2, 
    4: 2, 
    6: 1  
}

print("--- Service Disponible ---")

for groupes_actuel in groupes_clients:
    print(f"\n[NOVEAU GROUPE] Prochaine groupe: {groupes_actuel} personnes .")
    
    
    table_attribuee = False 
    
    
    for taille_table in tables_disponibles:
        
        # Condição de validação de capacidade e disponibilidade
        if taille_table >= groupes_actuel and tables_disponibles[taille_table] > 0:
            print(f"--> OK: Mesa de {taille_table} lugares atribuída.")
            
            
            tables_disponibles[taille_table] -= 1
            
            # Atualização do estado e interrupção da pesquisa
            table_attribuee = True
            break
            
    
    if not table_attribuee:
        print("--> RECUSADO: Nenhuma mesa com capacidade suficiente. Grupo transferido para a fila de espera.")
        liste_attente.append(groupes_actuel)
        
    
    total_mesas_restantes = sum(tables_disponibles.values())
    print(f"--> STATUS DO INVENTÁRIO: Restam {total_mesas_restantes} mesas no total {tables_disponibles}.")


print("\n--- RELATÓRIO DE FIM DE SERVIÇO ---")
print(f"Fila de espera final: {liste_attente}")












