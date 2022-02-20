from flask import Flask
from flask import render_template


app = Flask(__name__)

catlist = [
    "https://i.pinimg.com/236x/99/fe/d9/99fed9c7fcd3c35a969753ff7b876ff4.jpg",
    "https://i.pinimg.com/236x/08/64/0b/08640b34412b64c5be6d0296bc6192cd.jpg",
    "https://i.pinimg.com/236x/8d/ef/9d/8def9d8327fd4f7931afa31e95832550.jpg",
    "https://i.pinimg.com/236x/b0/33/6d/b0336de8b6ca431d44e0ad5ed76b1dd8.jpg",
    "https://i.pinimg.com/236x/87/a8/a3/87a8a378128df67cc09df6eda20be10f.jpg",
    "https://i.pinimg.com/236x/b1/f8/51/b1f8518732040ee0c9f826b2d28ed633.jpg",
    "https://i.pinimg.com/236x/f6/d0/0a/f6d00a247fa38686475a7cbf6b1a641d.jpg",
    "https://i.pinimg.com/236x/66/11/f6/6611f6fa444611e0900428396f559ae4.jpg",
    "https://i.pinimg.com/236x/5b/7d/26/5b7d260d84328d2b07d82c4334d943f0.jpg",
    "https://i.pinimg.com/236x/2d/89/c6/2d89c663d27e49cf2bb0a281a7c3f7c7.jpg",
    "https://i.pinimg.com/236x/36/58/ab/3658ab22d1b07fb1684bd42fe17621be.jpg",
    "https://i.pinimg.com/236x/64/0a/fb/640afbb1ddd2a0be507a14e584aeecf9.jpg",
]

@app.route("/")
def home():    
    return render_template('catguess.html', title = "guess the cat",
                           cat1 = catlist[0], cat2 = catlist[1], cat3 = catlist[2], cat4 = catlist[3],
                           link1 = '/stage2', link2 = '/loser', link3 = '/loser', link4 = '/loser')

@app.route("/stage2")
def stage2():
    return render_template('catguess.html', title = "stage2",
                           cat1 = catlist[4], cat2 = catlist[5], cat3 = catlist[6], cat4 = catlist[7],
                           link1 = '/loser', link2 = '/stage3', link3 = '/loser', link4 = '/loser')

@app.route("/stage3")
def stage3():
    return render_template('catguess.html', title = "stage3",
                           cat1 = catlist[8], cat2 = catlist[9], cat3 = catlist[10], cat4 = catlist[11],
                           link1 = '/loser', link2 = '/loser', link3 = '/win', link4 = '/loser')

@app.route("/loser")
def loser():    
    return render_template('catguess.html', title = "you lost, guess the cat. again",
                           cat1 = catlist[0], cat2 = catlist[1], cat3 = catlist[2], cat4 = catlist[3],
                           link1 = '/stage2', link2 = '/loser', link3 = '/loser', link4 = '/loser')

@app.route("/win")
def win():
    return render_template('win.html', title = "you won", comment = "here, have my email: no_it's_personal@gmail.com")


app.run(host="127.0.0.1", port=8080, threaded=True)
