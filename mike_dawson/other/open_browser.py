# http://stackoverflow.com/questions/4216985/call-to-operating-system-to-open-url
# Open Web Broser#
import webbrowser

wb = webbrowser.open("https://ya.ru")
print(wb)

# system independed
#if sys.platform=='win32':
#    os.startfile(url)
#elif sys.platform=='darwin':
#    subprocess.Popen(['open', url])
#else:
#    try:
#        subprocess.Popen(['xdg-open', url])
#    except OSError:
#        print 'Please open a browser on: '+url
