Folder sorter
===============
This script can be used to help in making your downloads folder clean.

You can for example run it with the parameters 'Shows' and 'Breaking Bad'
and it will go through your downloads folder and move all episodes of Breaking Bad it finds
and sort them after seasons in a new folder called 'Shows'.
If the script can not find the season of the episode the show will be stored in the root of the new folder.
This could also be done with movies, for example to get all Lord of the rings movies together in one folder.
If the downloads folder contains subtitle files for the episode/movie being looked for they are also moved to the correct place.
When the script has found all matching episodes it removes all empty folders from the downloads directory.

The script also moves all images and music files to folders called 'All Music' and 'All Images'
it might be a good idea then to connect the iTunes library to these folders to have access to all your
music and images.


The script also removes all .txt, .rar, .nfo files found in the downloads folder.

Example usages:
 - ./folder_sorter Shows 'Game of Thrones'
 - ./folder_sorter Movies 'Captain America'
 - ./folder_sorter 'Bad movies' 'Bring it on'
 - ./folder_sorter Homework 'Girl gone wild'
