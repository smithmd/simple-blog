# Simple Blog

A simple static blogging platform built on Flask.

Put markdown files in `/static/md_<content_type>` to show them on a site.

Visiting the route at `/b/<content_type>` lists all available files in the folder `/static/md_<content_type>`.

Visiting the route at `/b/<content_type>/<entry>` shows the contents of the file `/static/md_<content_type>/<entry>.md`, rendered from markdown. 