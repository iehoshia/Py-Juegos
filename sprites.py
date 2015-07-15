sprites.add(segmento)
 
  
reloj = pygame.time.Clock()
hecho = False
  
while not hecho:
      
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
  
        # Establecemos la velocidad basándonos en la tecla presionada
        # Queremos que la velocidad sea la suficiente para mover un segmento
        # más el margen.
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                cambio_x = (largodel_segmento + margendel_segmento) *- 1
                cambio_y = 0
            if evento.key == pygame.K_RIGHT:
                cambio_x = (largodel_segmento + margendel_segmento)
                cambio_y = 0
            if evento.key == pygame.K_UP:
                cambio_x = 0
                cambio_y = (altodel_segmento + margendel_segmento) *- 1
            if evento.key == pygame.K_DOWN:
                cambio_x = 0
                cambio_y = (altodel_segmento + margendel_segmento)
                       
    # Eliminamos el último segmento de la serpiente
    # .pop() este comando elimina el último objeto de una lista.
    segmento_viejo = segementos_dela_serpiente.pop()
    listade_todoslos_sprites.remove(segmento_viejo)
     
    # Determinamos dónde aparecerá el nuevo segmento
    x = segementos_dela_serpiente[0].rect.x + cambio_x
    y = segementos_dela_serpiente[0].rect.y + cambio_y
    segmento = Segmento(x, y)
     
    # Insertamos un nuevo segmento en la lista
    segementos_dela_serpiente.insert(0, segmento)
    listade_todoslos_sprites.add(segmento)
     
    # -- Dibujamos todo
    # Limpiamos la pantalla
    pantalla.fill(negro)
     
    listade_todoslos_sprites.draw(pantalla)
              
    # Actualizamos la pantalla
    pygame.display.flip()
      
    # Pausa
    reloj.tick(5)
                  
pygame.quit()