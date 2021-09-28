import win32com.client as win32

chrome = win32.Dispatch('chrome.application')

navegador = chrome.CreateItem(0)

