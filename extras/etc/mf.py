from copy import deepcopy

template = """
<div class="isotope-item" ontouchstart="this.classList.toggle(&#39;hover&#39;);">
    <div class="flipper">
        <div class="front">
            <img style="max-height: 300px" src="#img#">
            <p>#title#</p>
        </div>
        <div class="back">
            <p><strong><a href="#url#">#title#</a></strong></p>
            <p class="desc">#description#</p>
            <p><a href="#url#" class="btn btn-primary">Learn more</a></p>
        </div>
    </div>
</div>"""

featured = [
 {"title": "Citizen Kane", "src": "4806.c.jpeg",
  "blurb": "Program for Orson Welles' <i>Citizen Kane</i>, produced by RKO Pictures."},
 {"title": "The River", "src": "28087.c.jpeg",
  "blurb": "<b><i>The River</i></b><br /> Source: <b>United Artists Corporation</b>"},
 {"title": "Monsoon Wedding", "src": "49307.c.jpeg",
  "blurb": "<b><i>Monsoon Wedding</i></b><br /> Source: <b>Orfeo Films International</b>"},
 {"title": "Matewan", "src": "42030.c.jpeg",
  "blurb": "<b><i>U.S.A. : Matewan de John Sayles</i></b><br /> Source: <b>Cannes Film Festival</b>, 1987"},
 {"title": "Star wars spectacular", "src": "29146.c.jpeg",
  "blurb": "<b><i>Star wars spectacular</i></b><br /> Source: <b>Famous Monsters of Filmland</b>, c1977"},
]

for f in featured:
    x = deepcopy(template)
    docid, c, jpeg = f['src'].split('.')
    x = x.replace('#url#', f'/catalog/{docid}')
    x = x.replace('#description#', f['blurb'])
    x = x.replace('#title#', f['title'])
    x = x.replace('#img#', f['src'])
    print(x)