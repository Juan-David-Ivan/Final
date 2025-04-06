from crontab import CronTab
import os

def crear_tarea(min, hora, dia, mes, evento):

    cron = CronTab(user=True)

    script_path = os.path.join(os.getcwd(), 'recordatorio.sh')

    #crear una nueva tarea
    job = cron.new(command=f'{script_path} {evento}')

    #especificar fecha y hora
    job.minute.on(min)
    job.hour.on(hora)
    job.day.on(dia)
    job.month.on(mes)


    #guardar los cambios
    cron.write()