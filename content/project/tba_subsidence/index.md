---
title: Subsidence monitoring in transboundary aquifers
summary: I started processing interferometric synthetic aperture radar (InSAR) data in conflict settings in 2015 to measure subsidence patterns in transboundary aquifers. I include a short blog-style post introducing this work and where it stands today.

tags:
- InSAR
- Common pool resources
- Sentinel-1
- Groundwater
- Hydrology

date: "2020-08-06T00:00:00Z"
author: corey

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: "An environmental drill behind the US/Mexico border wall as construction of the new section of wall begins at the Organ Pipe National Monument, August 23, 2019. Photo credit: AZCentral.com"
  focal_point: Smart

links:
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

Some aquifers compact when groundwater is pumped out of water wells too quickly. Termed, “groundwater overdraft,” this overpumping causes the level of the ground to sink on the order of centimeters each year and is exemplified through this iconic photo illustrating the long-term implications of subsidence in California’s Central Valley.

<figure>
<img class="special-img-class" src="/img/land-subsidence-poland-calif-sized.jpg" width="200" height="400" />

<figcaption>Subsidence in the San Joaquin Valley, California. Photo credit: USGS</figcaption>
</figure>

In [transboundary aquifers](https://www.un-igrac.org/areas-expertise/transboundary-groundwaters) - regions where different diplomatic entities share groundwater - there is often a gap in the sharing of data across political boundaries, especially where those boundaries delimit geopolitical tension. A number of these aquifers are also the type of aquifer that will compact irreversibly due to groundwater overdraft.

<figure>
<img class="special-img-class" src="/img/tba_usmex_wb.png" />

<figcaption>Transboundary aquifers of the world and two that I highlighted in this study. The location of the drilling photo at the top of this post is marked in the lower left hand panel. Data: UN-International Groundwater Resource Assessment Center</figcaption>
</figure>

Drawing from political scientific research into the governing characteristics of political institutions that [successfully manage common pool resources](https://www.cambridge.org/core/books/governing-the-commons/A8BB63BC4A1433A50A3FB92EDBBB97D5), I sought to use methods in satellite radar remote sensing to fill a key characteristic of governing institutions for water sustainability: physically-based indicators of the condition of the shared resource across political boundaries.

In October 2019 I travelled to Valencia, Spain to give an [oral presentation](https://agu.confex.com/agu/19chapman5/meetingapp.cgi/Paper/488036) on monitoring subsidence in transboundary aquifers at the American Geophysical Union's Chapman Conference on the [Quest for Sustainability in Heavily Stressed Aquifers](https://connect.agu.org/aguchapmanconference/upcoming-chapmans/aquifers-sustainability).

To illustrate the potential value for diplomatic accountability using this technique, I ran subsidence analyses using data from the [Sentinel-1 constellation](https://sentinel.esa.int/web/sentinel/missions/sentinel-1) and the [Stanford Method for Persistent Scatterers](https://github.com/dbekaert/StaMPS) in two regions with shared aquifers and geopolitical tension: the US/Mexico border and the southern Jordan River Valley.

I found mean subsidence rates of 5 cm/year near a cluster of pivot-irrigated agricultural fields just on the Mexico side of the border with New Mexico. 

<figure>
<img class="special-img-class" src="/img/us_mexico_sub.png" />

<figcaption>Mean subsidence velocity at the US/Mexico border (2018)</figcaption>
</figure>

In the region of the Dead Sea, I found subsidence mirroring the political boundaries drawn during the [Oslo Accords](https://en.wikipedia.org/wiki/West_Bank_Areas_in_the_Oslo_II_Accord) around the ancient city of Jericho in the Israeli-occupied West Bank. Agricultural regions in Jericho subsided at a rate of 10 cm/year in 2018.

<figure>
<img class="special-img-class" src="/img/wb_subsidence.png" />

<figcaption>(Left) Setting image from Sentinel-2. (Middle) Boundaries drawn during the Oslo Accords and Israeli settlement outlines (blue). Area A is under Palestinian National Authority administration and Area C is controlled militarily by Israel. Area B, with mixed administration, is not included in the study region. (Right) Mean subsidence velocity in the southern Jordan River Valley (2018). Subsidence is focused along the movement barrier (a ditch to prevent vehicle crossings) in Jericho and in Jordan, near the Dead Sea. </figcaption>
</figure>

Subsidence around Jericho is likely driven by Palestinian reliance on groundwater resources from shallow Holocene alluvial aquifers underlaying agricultural regions of date palm cultivation in eastern Jericho. Interestingly, in regions of date palm cultivation under the control of Israeli settlers, there is not such dramatic subsidence. 

In their research on the political role of date palm agriculture in the West Bank, [Julie Trottier, *et al*](https://journals.sagepub.com/doi/abs/10.1177/2514848619876546), explain that the Israeli Water Authority and Israeli settlers are advancing recycled wastewater infrastructure for agricultural irrigation but Palestinian farmers are reduced to pumping shallow saline groundwater. It is possible that Palestinian reliance on shallow groundwater resources is driving the subsidence we see in the eastern regions of Jericho.

In my doctoral dissertation, I will argue that subsidence monitoring in transboundary aquifers can be used, where applicable, for a physically-based monitor of aquifer condition in pursuit of transparency, accountability, and sustainability of shared water in stressed aquifers. 

I started this work in 2015, conducting my first time series analysis of subsidence using Sentinel-1 data acquired over the Israeli-occupied West Bank. The first map I [published](https://www.guerrillacartography.org/atlases-shop/water-an-atlas) was with Guerrilla Cartography, comparing measured subsidence patterns to United Nations data on the demolition of Palestinian water wells and cisterns by the Israeli military. I continued with this work in 2016 and 2017 thanks to the support of [Professor David Saah](https://www.usfca.edu/faculty/david-saah) at the University of San Francisco and gave a [presentation](https://ui.adsabs.harvard.edu/abs/2017AGUFM.H11B1176S/abstract) on remote monitoring of groundwater overdraft using data from the Gravity Recovery and Climate Experiment (GRACE) and Sentinel-1 InSAR. 

Today, I continue with this work as a component of my dissertation research investigating physical aspects of war and conflict from the vantage point of satellite radar.

