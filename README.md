# About Glass Dome

Inspired by Jeff Huang's [Designed to Last](https://jeffhuang.com/designed_to_last/), Glass Dome is an effort to prevent link rot inside markdown notes.

It uses the Internet Archive's Wayback Machine and your own Dropbox account to preserve three kinds of link:

- Webpages
- Images
- Other files

## Setup

👉 You need [Alfred](https://www.alfredapp.com) with its payed *Powerpack* to use this workflow. For years now, Alfred has been the single most important productivity app on all my macs, so I couldn't recommend it enough.

To use image and attachment functionality, you'll also need a (free) Dropbox account. The web archiving feature doesn't need anything and works out of the box.

[Download the workflow file](https://github.com/macedotavares/Glass-Dome/raw/master/Glass%20Dome.alfredworkflow), double-click on it and define the following two variables in the dialog that pops up:

**db_token** (Dropbox Token)

Fill in "db_token" with your Dropbox authorization token. Go here:

https://www.dropbox.com/developers/apps?_ad=topbar4&_camp=myapps&_tk=pilot_lp

Create an app (name it whatever you like) and generate a token.

**db_folder** (Dropbox Folder)

This is the folder in which Glass Dome will place your uploaded files and images. If it doesn't exist, it will be automatically created on first use.

Files are never overwritten: they are timestamped to the second, and the API call is set to auto-rename.

## How to use

Each of the three actions is triggered by a keyword (feel free to change those, by the way).

- gdw (Webpage): It creates Wayback Machine snapshots of any URL passed to it and returns markdown links for both live and saved versions. If no URL is passed, it tries to detect the frontmost Safari tab.

- gdi (Image): Gets selected image file (in Finder) and copies it to a folder in Dropbox (you have to set in the workflow's Environment Variables). Then, it returns a markdown image link to that file. You can pass it an optional description that will be used as alt-text.

- gdf (File): Pretty much the same as the previous one, but for any other file type.

## A couple of warnings
1. This is a very basic workflow put together in a day, with very limited programming knowledge. I made it for my own use, but then figured it might be useful to someone else. It's not elegantly crafted, and it won't be regularly maintained. It seems to work, though.
2. I can't imagine how this workflow could break anything. But I may be wrong.

## Comments or suggestions?

Email: mail@senhortavares.com
Twitter: @senhortavares
