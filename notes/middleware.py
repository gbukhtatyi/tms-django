from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve

class LatestNotes(MiddlewareMixin):
    def process_request(self, request):
        current_url = resolve(request.path_info)

        if ('note-view' != current_url.url_name):
            return

        note_latest = request.session.get("note_latest", [])

        note_uuid = current_url.kwargs['note_uuid']
        if (note_uuid in note_latest):
            note_latest.remove(note_uuid)

        note_latest.append(note_uuid)
        note_latest = note_latest[-20:]
        request.session['note_latest'] = note_latest
        request.session['note_latest_count'] = len(note_latest)

