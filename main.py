from flask import Flask, render_template, request

main = Flask(__name__)


sozluk = {
    'programlama dili': 'Programlama dili, yazılımcının bir algoritmayı ifade etmek amacıyla, bir bilgisayara ne yapmasını istediğini anlatmasının tektipleştirilmiş yoludur.' ,
    'yazılım': 'Yazılım, elektronik aygıtların belirli bir işi yapmasını sağlayan programların tümüne verilen isimdir.' ,
    'python' : 'Web uygulamaları, yazılım geliştirme, veri bilimi ve makine öğreniminde (ML) yaygın olarak kullanılan bir programlama dilidir.' ,
    'bilgisayar' : 'Bilgisayar, aritmetik veya mantıksal işlem dizilerini (berim) otomatik olarak yürütmek üzere programlanabilen dijital bir elektronik makinedir.' ,
    'flask': 'Python programlama dilinde uygulama geliştirmek için kullanılan bir küçük ölçekli bir web çerçevesi modülüdür.'
}

@main.route('/', methods=['GET', 'POST'])
def index():
    anlam = ''
    kelime = ''
    
    if request.method == 'POST':
        kelime = request.form['kelime'].lower()  
        anlam = sozluk.get(kelime, 'Bu kelime sözlükte bulunmamaktadır.')  
    
    return render_template('index.html', anlam=anlam, kelime=kelime)

if __name__ == '__main__':
    main.run(debug=True)