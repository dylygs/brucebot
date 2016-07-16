from lxml import html
import requests

SONG_PAGE = "http://www.azlyrics.com/s/springsteen.html"

page = requests.get("http://www.mandatory.com/2013/05/07/the-50-greatest-bruce-springsteen-songs-of-all-time/")
tree = html.fromstring(page.content)

songs = []

for n in range(1, 51):
    songs.append(str(tree.xpath("//html/body/div[2]/div[3]/div/div[2]/div[1]/div[1]/strong[" + str(n) + "]/a/text()")).strip("[]\"',").replace("\\", "").lower())

#print(songs)

def getSongText(songurl):
    songPage = requests.get(songurl, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    songTree = html.fromstring(songPage.content)
    songContent = songTree.xpath("/html/body/div[3]/div/div[2]/div[6]/text()") 

    for line in songContent:
        if len(line.strip()) <= 5:
            songContent.remove(line)

    #for line in songContent:
    #    print(line.strip())

    songFile = open("songs/" + getFileNameFromLink(songurl), "w+")
    for line in songContent:
        songFile.write(str(line.strip()) + "\n")
    songFile.close()

def getFileNameFromLink(songurl):
    linkMod = songurl.split("/") # split the url by slashes to isolate the azlyrics filename
    lastPart = linkMod[-1] # store the last element of the list in lastPart, which is the azlyrics file name
    fileName = lastPart.split(".")[0] + ".txt" # replace the .html with .txt
    return fileName

def findSongs():
    songListPage = requests.get("http://www.azlyrics.com/s/springsteen.html", headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    songListTree = html.fromstring(songListPage.content)
    for n in range(2, 347):
        name = str(songListTree.xpath("/html/body/div[3]/div/div[2]/div[4]/a[" + str(n) + "]/text()")).lower().strip("[]\"'")

        if name in songs:
            #print("http://azlyrics.com" + str(songListTree.xpath("/html/body/div[3]/div/div[2]/div[4]/a[" + str(n) + "]/@href")).strip("[]\"'.."))
            getSongText("http://azlyrics.com" + str(songListTree.xpath("/html/body/div[3]/div/div[2]/div[4]/a[" + str(n) + "]/@href")).strip("[]\"'.."))

#getSongText("http://www.azlyrics.com/lyrics/brucespringsteen/blindedbythelight.html")
findSongs()
