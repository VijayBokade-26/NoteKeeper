### Features — keep it focused
Here's exactly what to build — nothing more, nothing less:
Core features that show Django skill

1. One — User registration and login with JWT. Every note belongs to a user, users only see their own notes.
2. Two — Full CRUD for notes. Create, read, update, delete. Each note has a title, content, and created_at timestamp.
3. Three — Tag system. A note can have multiple tags like "work", "personal", "ideas." This shows you understand many-to-many relationships in Django ORM.
4. Four — Search notes by title or content. Simple but shows you can write filtered querysets.
5. Five — Pin important notes. A boolean field that moves pinned notes to the top of the list.
6. Six — Soft delete. Instead of permanently deleting, mark notes as deleted and have a trash endpoint to recover them. This is something real production apps do and most beginners never implement.
Things that make it look production-ready
7. Seven — Proper validation and error responses throughout.
8. Eight — Pagination on the notes list endpoint.
9. Nine — Tests written for at least the main endpoints.
10. Ten — Dockerized with a proper README and live deployed URL.

