# ecoDev

Authors: [Conor Floyd](https://github.com/cfloyd-hmc), [Max McKnight](https://github.com/MaxistheSpy), [Peter Sullivan](https://github.com/Peter-Sully)

Created for 5c Hackathon

ecoDev is a game targeted at children, where they take pictures of plants in their area to try and fill out their ecoDex with as many local native plants as possible.

We approached the Sustainable Earth project track, and would like to apply to the "Outside of the Box" and "Beginners" overlays. Studies have shown that children prioritize virtual biodiversity over local biodiversity, so our app aims to get kids interested in their local wildlife by creating an interactive virtual way of interacting and learning about their native plants. We aimed to do this by creating a regional "ecoDex" of native plants that kids could fill out by taking pictures of plants. We did this with Kivy in Python, which we used for our overall GUI as well as camera. The picture is sent to the Pl@ntNet API (which identifies plants in a PNG) to get their scientific name. We then use the NatureServe Explorer REST API to find common names, detailed descriptions, and native locations based on the plant's scientific name. We designed our project with ethics in mind in a few ways in addition to just its purpose. In particular, we considered data privacy concerns with accidentally storing sensitive information from the users' photos, and are avoiding storing photos for that reason. We also considered the potential of spreading misinformation (eg. negative sentiment towards certain plants) by showing unfiltered plant descriptions from an API, which is why we decided to use NatureServe API as it is a trusted non-profit for wildlife conservation data.

People's empathy towards their local environment as children substantially affects their attitudes in adulthood. Our app would help create sustainability-minded adults, improving ecological education and connectedness in local communities. It would do this by utilizing many of the same strategies that cause kids to have strong anthropomorphic feelings towards virtual biodiversity, but now targeted at their native species. It would also help make ecological education less abstract, and create excitement about native plants.

## Planned Features
* Functional gui
* Fun cartoon caricatures based on plants
* Distinction between native and invasive species
* Distinct regional ecoDexes (reflects native plants actually near you)

## How to run
Our mockup of our main gui is in kivyMenubar.py. To try out the camera/plant recognition features, run kivyCam.py. 