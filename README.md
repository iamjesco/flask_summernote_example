
# Flask blog with Summernote

Summernote is a Rich Text Editor written primarily in bootstrap/js/jquery. 
There are a several other Rich text editor pluggins I could've used, like CKEditor for example. 
But the one thing I like about Summernote is that you can just upload images to your post without needing 
any extra code. It all just gets saved in Html code. (with the added text formatting) 
Less of a hassle and a quick fix. 

### Summernote issues

* Still have not figured out how to update the Summernote text current. Current workaround is to copy/paste the whole text block/paragraph.
* Posts will have to start with a block/paragraph of text. If the Feed posts are displaying a part of intro text. Otherwise the post will show up empty.
* Add only the jquery files to the index.html file. The old Bootstrap version CDN will fuck with the new BS5 one.











