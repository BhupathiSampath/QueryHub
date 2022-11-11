import operator
from functools import reduce
from django.db.models import Q
from datetime import date, timedelta


def text_search2(search, obj):
    print("Search:", search)
    obj = obj.filter(
        Q(
            reduce(
                operator.and_,
                (Q(lineage__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.and_,
                (Q(division__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.and_,
                (Q(clade__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.and_,
                (Q(strain__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.and_,
                (Q(aadeletions__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.and_,
                (Q(nextclade_pango__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.and_,
                (Q(aasubstitutions__icontains=x) for x in search),
            )
        )
    )
    return obj


def text_search(search, obj):
    obj = obj.filter(
        Q(clade__in=search)
        | Q(strain__in=search)
        | Q(lineage__in=search)
        | Q(division__in=search)
        | Q(aadeletions__in=search)
        | Q(nextclade_pango__in=search)
        | Q(aasubstitutions__in=search)
    )
    return obj


def text_search1(search, obj):
    print("Search:", search)
    obj = obj.filter(
        Q(date__icontains=search[0])
        | Q(lineage__icontains=search[0])
        | Q(division__icontains=search[0])
        | Q(strain__icontains=search[0])
        | Q(nextclade_pango__icontains=search[0])
        | Q(aasubstitutions__icontains=search[0])
        | Q(aadeletions__icontains=search[0])
        | Q(clade__icontains=search[0])
    )
    return obj


def advenced_filter(
    obj,
    days,
    date,
    clade,
    strain,
    lineage,
    present,
    division,
    aadeletions,
    nextclade_pango,
    aasubstitutions,
):
    if days and present == False:
        last_date = QueryHubModel.objects.values("date").latest("date")
        day = last_date["date"] - timedelta(days=int(days))
        obj = obj.filter(date__gte=day)
    if days and present == True:
        day = datetime.date.today() - timedelta(days=int(days))
        obj = obj.filter(date__gte=day)
    if date:
        obj = obj.filter(date=date)
    if clade:
        obj = obj.filter(clade__in=clade)
    if strain:
        obj = obj.filter(strain__in=strain)
    if lineage:
        obj = obj.filter(lineage__in=lineage)
    if division:
        obj = obj.filter(division__in=division)
    if nextclade_pango:
        obj = obj.filter(nextclade_pango__in=nextclade_pango)
    if aadeletions:
        obj = obj.filter(
            reduce(
                operator.and_,
                (Q(aadeletions__icontains=x) for x in aadeletions),
            )
        )
    if aasubstitutions:
        obj = obj.filter(
            reduce(
                operator.and_,
                (Q(aasubstitutions__icontains=x) for x in aasubstitutions),
            )
        )
    return obj
