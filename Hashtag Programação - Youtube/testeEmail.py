import win32com.client as win32 

outlook = win32.Dispatch('outlook.application') 

email = outlook.CreateItem(0)

email.To = '**'
email.Subject = 'Teste automatizado do Lucas'
email.HTMLBody = """
<p>Olá Lucas</p>
<p>Esse foi o teste</p>
<p>Espero que tenha dado certo</p>
<p>Valeu</p>
<p>Abraços</p>
"""

anexo = "D:\GoogleDrive\Documentos\PESSOAL\PYTHON\Hashtag Programação - Youtube\março.xlsx"
email.Attachments.Add(anexo)

email.Send()
print('Enviado')