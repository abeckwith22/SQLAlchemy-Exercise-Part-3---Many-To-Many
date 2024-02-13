# Many-to-Many - Blogly

#### Part Three: Add M2M relationship
Tags should have an:
- [X] **id**, like for **User**
- [X] **name**, (unique!)

#### User Interface
- [X] Add Tag
- [X] Edit Tag
- [X] List Tag
- [X] Show Tag
- [X] Show Posts with Tags
- [X] Edit Posts with Tags
- [X] Show Posts with Tags


#### Add Routes
- [X] **GET** /tags : List all tags, with links to the tag detail page.
- [X] **GET** /tags/[*tag-id*] : Show detail about a tag. Have links to edit form and to delete.
- [X] **GET** /tags/new : Shows a form to add a new tag.
- [X] **POST** /tags/new : Process add form, adds tag, and redirect to tag list.
- [X] **GET** /tags/[*tag-id*]/edit : Show edit form for a tag
- [X] **POST** /tags/[*tag-id*]/edit : Process edit form, edit tag, and redirects to the tags list.
- [X] **POST** /tags/[*tag-id*]/delete : Delete a tag.

