import os
def summarize_insights(market_data, plan):
    lines=['Market Intelligence Summary (Egypt — Construction):','']
    for x in market_data[:10]:
        if x.get('type')=='tender':
            lines.append(f"- TENDER: {x['title']} — deadline {x['deadline']} — {x['scope']}")
        elif x.get('type')=='competitor':
            lines.append(f"- COMPETITOR: {x['name']} — {x['change']}")
        else:
            lines.append(f"- MATERIAL: {x['material']} — {x['price_change']} ({x['note']})")
    lines.append(''); lines.append(f'Plan: {plan}. Delivery: email + WhatsApp (if enabled).')
    return "\n".join(lines)
