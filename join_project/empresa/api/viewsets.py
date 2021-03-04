# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from django.db.models import Count
from datetime import datetime

from empresa.api.serializers import AlvosSerializer
from empresa.models import Funcionarios, Alvos


# Create your viewsets here.
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def list(self, request, *args, **kwargs):
        try:
            queryset_1 = Funcionarios.objects.all().order_by('admissao').values('nome', 'cargo__nome_cargo', 'admissao')
            result_queryset_1 = [funcionario for funcionario in queryset_1]

            queryset_2 = Funcionarios.objects.all().order_by('admissao').values('nome', 'cargo__nome_cargo',
                                                                                'admissao')[:1]
            result_queryset_2 = [funcionario for funcionario in queryset_2]

            queryset_3 = Funcionarios.objects.values('cargo__nome_cargo').annotate(qtd_funcionarios=Count('cargo'))
            result_queryset_3 = [funcionario for funcionario in queryset_3]

            print(result_queryset_1)
            print(result_queryset_2)
            print(result_queryset_3)

            return Response({"message": "ok"}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"message": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AlvosViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None
    permission_classes = [AllowAny]
    authentication_classes = []

    def list(self, request, *args, **kwargs):
        try:
            queryset = Alvos.objects.filter(deletado=False).order_by('data_expiracao')
            serializer = AlvosSerializer(queryset, many=True)

            return Response({"alvos": serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"message": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            exceptions = []

            if not 'nome' in data or data['nome'] in ['', None]:
                exceptions.append('nome')

            if not 'latitude' in data or data['latitude'] in ['', None]:
                exceptions.append('latitude')

            if not 'longitude' in data or data['longitude'] in ['', None]:
                exceptions.append('longitude')

            if not 'data_expiracao' in data or data['data_expiracao'] in ['', None]:
                exceptions.append('data_expiracao')

            if not exceptions:
                ano, mes, dia = data['data_expiracao'][0:10].split("-")
                data_expiracao = datetime(int(ano), int(mes), int(dia))
                new_alvo = Alvos.objects.create(
                    nome=data['nome'],
                    latitude_localizacao=data['latitude'],
                    longitude_localizacao=data['longitude'],
                    data_expiracao=data_expiracao
                )

                return Response({"message": "Alvo registrado com sucesso!", "id": new_alvo.id}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Campos obrigatórios não preenchidos!", "exceptions": exceptions}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({"message": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            data = request.data
            exceptions = []

            if not 'nome' in data or data['nome'] in ['', None]:
                exceptions.append('nome')

            if not 'latitude' in data or data['latitude'] in ['', None]:
                exceptions.append('latitude')

            if not 'longitude' in data or data['longitude'] in ['', None]:
                exceptions.append('longitude')

            if not 'data_expiracao' in data or data['data_expiracao'] in ['', None]:
                exceptions.append('data_expiracao')

            if not exceptions:
                ano, mes, dia = data['data_expiracao'][0:10].split("-")
                data_expiracao = datetime(int(ano), int(mes), int(dia))
                Alvos.objects.filter(id=kwargs['pk']).update(
                    nome=data['nome'],
                    latitude_localizacao=data['latitude'],
                    longitude_localizacao=data['longitude'],
                    data_expiracao=data_expiracao
                )

                return Response({"message": "Alvo atualizado com sucesso!", "id": kwargs['pk']}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Campos obrigatórios não preenchidos!", "exceptions": exceptions}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({"message": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            queryset = Alvos.objects.filter(id=kwargs['pk'])

            if queryset:
                queryset.update(deletado=True)
                return Response({"message": "Alvo deletado com sucesso!", "id": queryset.first().id}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Alvo não existe!"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return Response({"message": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)