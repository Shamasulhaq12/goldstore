from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from decimal import Decimal
from .models import Account, BalanceReport, GoldPrice
from rest_framework.permissions import IsAuthenticated
from .serializers import AccountSerializer, GoldPriceSerializer, BalanceReportSerializer


class GoldPriceViewSet(viewsets.ModelViewSet):
    allowed_methods = ['GET', 'POST', 'PUT']
    queryset = GoldPrice.objects.all()
    serializer_class = GoldPriceSerializer
    permission_classes = [IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]


class BalanceReportViewSet(viewsets.ModelViewSet):
    queryset = BalanceReport.objects.all()
    serializer_class = BalanceReportSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        payable = request.data.get('payable', None)
        receivables = request.data.get('receivable', None)
        gold_price = request.data.get('gold_price', None)
        rati = request.data.get('rati', None)
        _type = request.data.get('type', None)
        gold = 0.000
        cash_in = 0.000
        cash_out = 0.000
        try:
            balance = request.user.balance
            gold_price = GoldPrice.objects.get(id=gold_price)
            if _type == "gold":
                if payable:
                    impure_gold = round(
                        Decimal(payable)/Decimal(96)*Decimal(rati), 3)
                    gold = payable - impure_gold
                    balance -= payable
                elif receivables:
                    impure_gold = round(Decimal(receivables) /
                                        Decimal(96)*Decimal(rati), 3)
                    gold = receivables - impure_gold
                    balance += receivables
            elif _type == "cash":
                if payable:
                    gold = round(Decimal(payable)/Decimal(gold_price)
                                 * Decimal(11.664), 3)
                    balance -= gold
                    cash_out = payable
                elif receivables:
                    gold = round(Decimal(receivables) /
                                 Decimal(gold_price)*Decimal(11.664), 3)
                    balance += gold
                    cash_in = receivables
            data = request.data
            data['gold'] = gold
            data['cash_in'] = cash_in
            data['cash_out'] = cash_out

            request.user.balance = balance
            request.user.save()
            serializer = BalanceReportSerializer(
                data=data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        payable = request.data.get('payable', None)
        receivables = request.data.get('receivable', None)
        gold_price = request.data.get('gold_price', None)
        rati = request.data.get('rati', None)
        _type = request.data.get('type', None)
        gold = 0.000
        cash_in = 0.000
        cash_out = 0.000
        try:
            balance = request.user.balance
            if _type == "gold":
                if payable:
                    impure_gold = round(
                        Decimal(payable)/Decimal(96)*Decimal(rati), 3)
                    gold = payable - impure_gold
                    balance = payable
                elif receivables:
                    impure_gold = Decimal(receivables) / \
                        Decimal(96)*Decimal(rati)
                    gold = receivables - impure_gold
                    balance = receivables
            elif _type == "cash":
                if payable:
                    gold = round(Decimal(payable)/Decimal(gold_price)
                                 * Decimal(11.664), 3)
                    balance = gold
                    cash_out = payable
                elif receivables:
                    gold = round(Decimal(receivables) /
                                 Decimal(gold_price)*Decimal(11.664), 3)
                    balance = gold
                    cash_in = receivables
            data = request.data
            data['gold'] = gold
            request.user.balance = balance
            request.user.save()
            data['cash_in'] = cash_in
            data['cash_out'] = cash_out
            instance = self.get_object()
            serializer = BalanceReportSerializer(
                instance, data=data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        account = self.request.query_params.get('account', None)
        queryset = BalanceReport.objects.all()
        if account:
            queryset = BalanceReport.objects.filter(account=account)
        serializer = BalanceReportSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
