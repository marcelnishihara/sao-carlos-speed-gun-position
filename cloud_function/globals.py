source = "https://saocarlosagora.com.br/"
regex = r".*radar.>.*<ul>.*<li><big>([0-9]{2}).*<h4>(.*)<\/h4>.*<li><big>([0-9]{2}).*<h4>(.*)<\/h4>.*<li><big>([0-9]{2}).*<h4>(.*)<\/h4>"

colors = {
    "err" : "\033[91m",
    "end" : "\033[m",
    "success" : "\033[92m",
    "warning" : "\033[93m"
}