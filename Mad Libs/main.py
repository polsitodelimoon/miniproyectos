def hist1():
    persona=input('Ingrese una persona: ')
    advTiempo=input('Ingrese un adverbio de tiempo: ')
    lugar=input('Ingrese un lugar: ')
    animal=input('Ingrese un animal: ')
    comida=input('Ingrese una comida: ')
    color=input('Ingrese un color: ')
    adverbio=input('Ingrese un adbervio de cantidad: ')
    cosa=input('Ingrese una cosa: ')

    parte1= f'Un día estaba paseando con mi {animal} y me encontré a {persona}. Hacía {adverbio} tiempo que no le veía.'
    parte2= f'De repente, mi {animal} se puso a defecar. Pero no parecía una caca normal, más bien se parecía a un/a {cosa}. Y además tenía un color {color}.'
    parte3= f'Pensé que podría haber sido por el/la {comida} que le di {advTiempo}. Luego nos despedimos y me fui ya al {lugar}'
    print('----------------------')
    print(parte1,parte2,parte3)


if __name__=='__main__':
    hist1()