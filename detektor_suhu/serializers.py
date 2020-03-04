from detektor_suhu.models import Stats

class StartSerializer(selrializers.Modelserializer):
    class Meta:
      model = Stats
      fields = '__all__'