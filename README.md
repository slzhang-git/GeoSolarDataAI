# Geosolar

We release an API named Geosolar. Particularly, for any user‑specified building location, our API automatically retrieves the corresponding satellite imagery from open-source aerial imagery sources, detects rooftop solar panels, and returns georeferenced panel polygons that can be directly used in maps and programming works.

We show an example of solar panel detection for a single building in the city of Zurich in Switzerland in [this html file](https://github.com/slzhang-git/GeoSolarDataAI/blob/main/example_Zurich.html), where we store all the geographic geometry of the detected panels at line 138 of the file. The visualization of the detected solar panels is below, and we also show the detected panel in an [interactive map](https://slzhang-git.github.io/GeoSolarDataAI/example_Zurich.html).

<img width="1378" height="1067" alt="example" src="https://github.com/user-attachments/assets/7ea129ba-98c3-49d7-9ae2-831c698558b0" />


**Below is a python programming example for using our API in Google Colab environment:**

```python
!pip install cenergy

from cenergy3 import generate_3d_model, plot_3d_model, save_3d_model

api_key = "123456789123456789123456789" # please change to your own OpenTopography API key, which is free can can be obtained from http://opentopography.org/
target_place = "Rousay-Orkney Islands-Scotland" # You can change to the name of the place you want

fig_json = generate_3d_model(api_key=api_key, target_place=target_place)
plot_3d_model(fig_json)
save_3d_model(fig_json)
```
