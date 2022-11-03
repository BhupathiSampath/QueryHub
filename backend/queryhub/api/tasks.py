def text_search(search, obj):
    obj = obj.filter(
        Q(date__icontains=search)
        | Q(lineage__icontains=search)
        | Q(division__icontains=search)
        | Q(strain__icontains=search)
        | Q(nextclade_pango__icontains=search)
        | Q(aasubstitutions__icontains=search)
        | Q(aadeletions__icontains=search)
        | Q(clade__icontains=search)
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
        obj = obj.filter(clade__in=clade.split(","))
    if strain:
        obj = obj.filter(strain__in=strain.split(","))
    if lineage:
        obj = obj.filter(lineage__in=lineage.split(","))
    if division:
        obj = obj.filter(division__in=division.split(","))
    if nextclade_pango:
        obj = obj.filter(nextclade_pango__in=nextclade_pango.split(","))
    if aadeletions:
        obj = obj.filter(
            reduce(
                operator.and_,
                (Q(aadeletions__icontains=x) for x in aadeletions.split(",")),
            )
        )
    if aasubstitutions:
        obj = obj.filter(
            reduce(
                operator.and_,
                (Q(aasubstitutions__icontains=x) for x in aasubstitutions.split(",")),
            )
        )
    return obj
