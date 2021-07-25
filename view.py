import eel
import desktop
import search
import save

app_name="web"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word, csv_file, save_folder):
    search_result = search.kimetsu_search(word, csv_file)
    save.save_csv(save_folder, csv_file)
    return search_result


desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)