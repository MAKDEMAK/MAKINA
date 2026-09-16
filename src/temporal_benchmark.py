"""Minimal reproducible benchmark for temporal-in-sensor-processing.
Digital emulation only: it does not claim hardware energy/performance.
"""
from __future__ import annotations
import csv, json, math, random
from pathlib import Path


def signal(n=2000, dt=0.001, seed=7):
    r=random.Random(seed); xs=[]
    for i in range(n):
        t=i*dt
        base=0.15*math.sin(2*math.pi*3*t)
        pulses=sum(a*math.exp(-((t-c)/0.012)**2) for c,a in [(0.25,1.0),(0.72,.7),(1.25,1.2),(1.63,.85)])
        xs.append((t,base+pulses+r.gauss(0,.015)))
    return xs


def uniform(samples):
    return [{"t":t,"a":x} for t,x in samples]


def threshold_events(samples, threshold=.12):
    out=[]; prev=samples[0][1]
    for t,x in samples[1:]:
        d=x-prev
        if abs(d)>=threshold:
            out.append({"t":t,"a":1 if d>0 else -1}); prev=x
    return out


def latency_fading(samples, threshold=.35, tau=.08):
    out=[]; state=0.0; last_t=samples[0][0]
    for t,x in samples:
        state*=math.exp(-(t-last_t)/tau); last_t=t
        if abs(x)>=threshold and abs(state)<.25:
            latency=max(1e-6, .02/(abs(x)+1e-6))
            out.append({"t":t+latency,"a":1 if x>0 else -1,"state":state})
            state=1.0 if x>0 else -1.0
    return out


def nearest_error_ms(events, truth=(.25,.72,1.25,1.63)):
    if not events: return None
    return 1000*sum(min(abs(e["t"]-q) for e in events) for q in truth)/len(truth)


def score(events, truth=(.25,.72,1.25,1.63), tol=.04):
    if not events: return 0.0
    hits=sum(any(abs(e["t"]-q)<=tol for e in events) for q in truth)
    return hits/len(truth)


def run(outdir="artifacts/temporal-benchmark"):
    s=signal(); variants={"conventional_uniform_sampling":uniform(s),"threshold_event_encoding":threshold_events(s),"latency_encoding_with_fading_state":latency_fading(s)}
    ref=len(variants["conventional_uniform_sampling"]); rows=[]
    for name,ev in variants.items():
        rows.append({"variant":name,"transferred_items":len(ev),"reduction_x":ref/max(1,len(ev)),"event_score":score(ev),"temporal_error_ms":nearest_error_ms(ev),"energy_status":"not_measured"})
    p=Path(outdir); p.mkdir(parents=True,exist_ok=True)
    (p/"metrics.json").write_text(json.dumps({"emulation":True,"hardware_energy_measured":False,"rows":rows},indent=2),encoding="utf-8")
    with (p/"comparison.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    with (p/"event_stream.jsonl").open("w",encoding="utf-8") as f:
        for name,ev in variants.items():
            for e in ev: f.write(json.dumps({"variant":name,**e})+"\n")
    return rows

if __name__=="__main__": run()
