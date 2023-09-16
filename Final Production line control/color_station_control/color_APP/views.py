from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from color_APP.models import *
from django.urls import reverse_lazy
import django.http
import json as JSON


class Stations(ListView):
    model = Station
    template_name = "station.html"


class Faults(ListView):
    model = Fault
    template_name = "faults.html"


class StationDetail(DetailView):
    model = Station
    template_name = 'stationdetail.html'


class FaultDetail(DetailView):
    model = Fault
    template_name = "faultdetail.html"


class StationCreate(CreateView):
    model = Station
    template_name = "stationcreate.html"
    fields = '__all__'


class ReportCreate(CreateView):
    model = Report
    fields = "__all__"
    template_name = 'reportcreate.html'

    # success_url='/'     
    def get_success_url(self):
        return reverse_lazy('stationdetail', args=(int(self.request.POST.get('station')),))


class FaultCreate(CreateView):
    model = Fault
    template_name = "faultcreate.html"
    fields = '__all__'


class StationUpdate(UpdateView):
    model = Station
    template_name = "stationupdate.html"
    fields = '__all__'


class FaultUpdate(UpdateView):
    model = Fault
    template_name = "faultupdate.html"
    fields = '__all__'


class ReportUpdate(UpdateView):
    model = Report
    template_name = 'reportupdate.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('stationdetail', args=(self.object.station.id,))


class StationDelete(DeleteView):
    model = Station
    template_name = "stationdelete.html"
    success_url = reverse_lazy('stations')


class FaultDelete(DeleteView):
    model = Fault
    template_name = "faultdelete.html"
    success_url = reverse_lazy('faults')


class ReportDelete(DeleteView):
    model = Report
    template_name = 'reportdelete.html'

    def get_success_url(self):
        return reverse_lazy('stationdetail', args=(self.object.station.id,))


class Pieces(ListView):
    model = Piece
    template_name = 'pieces.html'


class PieceCreate(CreateView):
    model = Piece
    template_name = 'piececreate.html'
    fields = '__all__'
    success_url = reverse_lazy('pieces')


class PieceUpdate(UpdateView):
    model = Piece
    template_name = 'pieceupdate.html'
    fields = '__all__'
    success_url = reverse_lazy('pieces')


class PieceDelete(DeleteView):
    model = Piece
    template_name = 'piecedelete.html'
    success_url = reverse_lazy('pieces')


class EquipCreate(CreateView):
    model = Equip
    template_name = 'equipcreate.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('stationdetail', args=(self.object.station.id,))


class EquipStation(DetailView):
    template_name = 'equipstation.html'
    model = Station


class StationReport(TemplateView):
    template_name = 'stationreport.html'


def stationsJson(request):
    len([1, 5])
    json = {}
    stations = Station.objects.all()
    for station in stations:
        json[station.name] = {}
        json[station.name]['equips'] = {}
        json[station.name]['reports'] = len(list(station.report_set.all()))
        for equip in station.equip_set.all():
            json[station.name]['equips'][equip.name] = len(list(equip.report_set.all()))
    return django.http.HttpResponse(JSON.dumps(json), content_type="application/json")


class EquipDetail(DetailView):
    model = Equip
    template_name = 'equipdetail.html'


class EquipDelete(DeleteView):
    model = Equip
    template_name = 'equipdelete.html'

    def get_success_url(self):
        return reverse_lazy('equipstation', args=(self.object.station.id,))


class EquipUpdate(UpdateView):
    model = Equip
    fields = '__all__'
    template_name = "equipupdate.html"

    def get_success_url(self):
        return reverse_lazy('equipstation', args=(self.object.station.id,))
