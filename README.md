# factsheets_sshoc_services

This is the Gitlab repository for the factsheets created within SSHOC WP3.6 for the Virtual Collection Registry and the Language Resource Switchboard.

In case of questions write to sbudden@gwdg.de

The files in this repository are Markdown files which contain - one service per file - the factsheets. All factsheets follow the same pattern and describe the service, its possible use case, point to other services in the SSHOC environment and illustrate all of this with examples.

# Documentation

This folder contains all static pages belonging to the factsheets_sshoc_services. They are all written in [Markdown](https://daringfireball.net/projects/markdown/).

## Naming schema

The files in this directory follow the naming scheme

        [pagename].[lang].md

Where `pagename` is the identifier used for the page. Supported languages are English and German, they are coded by their iso code, so `en` for English and `de` for German. The `.md` extension identifies the file as Markdown file.

The markdown files are later rendered as html within the factsheets_sshoc_services page in the location /docs/ identified by their `pagename`.

This means `syntax.en.md` is shown at <https://textgridrep.org/docs/syntax> if your language is English, `syntax.de.md` is shown if you switch to German.

Some more examples:
* [voyant.en.md](voyant.en.md) -> <https://textgridrep.org/docs/voyant> - choose lang English
* [voyant.de.md](voyant.de.md) -> <https://textgridrep.org/docs/voyant> - choose lang German
* [annotate.en.md](annotate.en.md) -> <https://dev.textgridrep.org/docs/annotate> - choose lang English
* [annotate.de.md](annotate.de.md) -> <https://dev.textgridrep.org/docs/annotate> - choose lang German

### index.en.md / index.de.md

An exception from the naming scheme is `index.en.md` or `index.de.md` which is not only available at <https://textgridrep.org/docs/index> but also at the root of the portal: <https://textgridrep.org> . If you want to refer to it do not use the `docs/index` location ;-).

## Deployment / development system: https://dev.textgridrep.org

If you make changes like changing or adding files these will be available automatically on the [development system](https://dev.textgridrep.org/) within at most half an hour. You will find your page by its pagename in the /docs/ folder, even if its not yet linked from anywhere. So a new page `testitest.en.md` will be visible at `https://dev.textgridrep.org/docs/testitest` if the language is English.

## Syntax

The Markdown syntax used is described in the [CommonMark Spec 0.29](https://spec.commonmark.org/0.29/).

### Linking between pages

Linking between pages is possible, adress them by their relative adress in the `/docs/` section. Refer to the syntax.[en/de].md document as to `/docs/syntax`. Example: 

```markdown
Find more info on the [syntax](/docs/syntax) page.
```
### Linking within pages / Heading anchors
The [Heading anchor](https://github.com/atlassian/commonmark-java#heading-anchor) extension is activated which generates IDs for heading elements. Which could be used as anchors, this means that you can link to them.

An Example:

A Marddown snippet

        # Eine Überschrift

        ## Eine Unterüberschrift 

will be rendered as HTML Elements

        <h1 id="eine-überschrift">Eine Überschrift</h1>
 
        <h2 id="eine-unterüberschrift">Eine Unterüberschrift</h2>

which means the ID will be lowercase with hyphens (`-`) instead of spaces. So you can link to them in Markdown like

        Siehe [Kapitel 1](#eine-überschrift) und [Kapitel 1.1](#eine-unterüberschrift)

Which allwos creation of a TOC for example. You can also reference headings or subheadings on other pages

        see the [voyant-example](/docs/voyant#beispiel)

If you are unsure which ID was generated for a heading inspect the element with the developer tool of your web browser. In Firefox for example you can do this with a click on the heading and the context menu entry "Inspect Element"("Element untersuchen"), which will reveal the id:

![inspecting the anchor id](images/inspect-anchor.png)


### Images

Own images can be placed in the `images` subfolder of this directory. They are referenced by their relative path like this:

```
  ![The reading owl](images/owl-reading.png)
```

This will be rendered as:

![The reading owl](images/owl-reading.png)

### Markdown parser in use / supported syntax / extensions

For parsing Markdwon and rendering HTML the [commonmark-java](https://github.com/atlassian/commonmark-java) library is used. Currently implemented by this library is the [CommonMark Spec 0.29](https://spec.commonmark.org/0.29/). Look at the [CommonMark Dingus](http://spec.commonmark.org/dingus/) for testing and previewing the syntax.

Currently there are two extensions activated, there are some [more available](https://github.com/atlassian/commonmark-java#extensions), if you need one just ask.

Active extensions:

* [Heading anchor](https://github.com/atlassian/commonmark-java#heading-anchor)
* [Tables](https://github.com/atlassian/commonmark-java#tables)
* [YAML front matter](https://github.com/atlassian/commonmark-java#yaml-front-matter)

If there is a need for even more extensions or different syntax we may painlessly switch to [flexmark-java](https://github.com/vsch/flexmark-java) for parsing, which is a commonmark-java fork wich supports a lot more different markdown flavours and extensions.

