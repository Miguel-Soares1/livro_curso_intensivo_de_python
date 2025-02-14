reserva = int(input('quantos lugares voce deseja reservar? '))
if reserva > 8:
    print(f'no momento não temos {reserva} lugares disponiveis, por favor, aguarde um momento.')
else:
    print('lugares reservados!')