Require Export Program.Basics. Open Scope program_scope.
Require Import paco5.
Set Implicit Arguments.

Section Companion5.

Variable T0 : Type.
Variable T1 : forall (x0: @T0), Type.
Variable T2 : forall (x0: @T0) (x1: @T1 x0), Type.
Variable T3 : forall (x0: @T0) (x1: @T1 x0) (x2: @T2 x0 x1), Type.
Variable T4 : forall (x0: @T0) (x1: @T1 x0) (x2: @T2 x0 x1) (x3: @T3 x0 x1 x2), Type.

Local Notation rel := (rel5 T0 T1 T2 T3 T4).

Variable gf: rel -> rel.
Hypothesis gf_mon: monotone5 gf.

(** 
  Compatibility, Companion & Guarded Companion
*)

Structure compatible5 (clo: rel -> rel) : Prop :=
  compat5_intro {
      compat5_mon: monotone5 clo;
      compat5_compat : forall r,
          clo (gf r) <5= gf (clo r);
    }.

Inductive cpn5 (r: rel) e0 e1 e2 e3 e4 : Prop :=
| cpn5_intro
    clo
    (COM: compatible5 clo)
    (CLO: clo r e0 e1 e2 e3 e4)
.

Definition gcpn5 := compose gf cpn5.

Lemma cpn5_mon: monotone5 cpn5.
Proof.
  red. intros.
  destruct IN. exists clo.
  - apply COM.
  - eapply compat5_mon; [apply COM|apply CLO|apply LE].
Qed.

Lemma cpn5_compat: compatible5 cpn5.
Proof.
  econstructor; [apply cpn5_mon|intros].
  destruct PR; eapply gf_mon with (r:=clo r).
  - eapply (compat5_compat COM); apply CLO.
  - intros. econstructor; [apply COM|apply PR].
Qed.

Lemma cpn5_greatest: forall clo (COM: compatible5 clo), clo <6= cpn5.
Proof. intros. econstructor;[apply COM|apply PR]. Qed.

Lemma cpn5_comp: forall r,
    cpn5 (cpn5 r) <5= cpn5 r.
Proof.
  intros. exists (compose cpn5 cpn5); [|apply PR].
  econstructor.
  - repeat intro. eapply cpn5_mon; [apply IN|].
    intros. eapply cpn5_mon; [apply PR0|apply LE].
  - intros. eapply (compat5_compat cpn5_compat).
    eapply cpn5_mon; [apply PR0|].
    intros. eapply (compat5_compat cpn5_compat), PR1. 
Qed.

Lemma gcpn5_mon: monotone5 gcpn5.
Proof.
  repeat intro. eapply gf_mon; [eapply IN|].
  intros. eapply cpn5_mon; [apply PR|apply LE].
Qed.

Lemma gcpn5_sound:
  paco5 gcpn5 bot5 <5= paco5 gf bot5.
Proof.
  intros.
  set (rclo := fix rclo clo n (r: rel) :=
         match n with
         | 0 => r
         | S n' => rclo clo n' r \5/ clo (rclo clo n' r)
         end).
  assert (RC: exists n, rclo cpn5 n (paco5 gcpn5 bot5) x0 x1 x2 x3 x4) by (exists 0; apply PR); clear PR.
  
  cut (forall n, rclo cpn5 n (paco5 gcpn5 bot5) <5= gf (rclo cpn5 (S n) (paco5 gcpn5 bot5))).
  { intro X. revert x0 x1 x2 x3 x4 RC; pcofix CIH; intros.
    pfold. eapply gf_mon.
    - apply X. apply RC.
    - intros. right. eapply CIH. apply PR.
  }

  induction n; intros.
  - eapply gf_mon.
    + _punfold PR; [apply PR|apply gcpn5_mon].
    + intros. right. eapply cpn5_mon; [apply PR0|].
      intros. pclearbot. apply PR1.
  - destruct PR.
    + eapply gf_mon; [eapply IHn, H|]. intros. left. apply PR.
    + eapply gf_mon.
      * eapply (compat5_compat cpn5_compat).
        eapply (compat5_mon cpn5_compat); [apply H|apply IHn].
      * intros. econstructor 2. apply PR.
Qed.

(** 
  Recursive Closure & Weak Compatibility
*)

Inductive rclo5 (clo: rel->rel) (r: rel): rel :=
| rclo5_base
    e0 e1 e2 e3 e4
    (R: r e0 e1 e2 e3 e4):
    @rclo5 clo r e0 e1 e2 e3 e4
| rclo5_clo'
    r' e0 e1 e2 e3 e4
    (R': r' <5= rclo5 clo r)
    (CLOR': clo r' e0 e1 e2 e3 e4):
    @rclo5 clo r e0 e1 e2 e3 e4
| rclo5_step'
    r' e0 e1 e2 e3 e4
    (R': r' <5= rclo5 clo r)
    (CLOR': @gf r' e0 e1 e2 e3 e4):
    @rclo5 clo r e0 e1 e2 e3 e4
| rclo5_cpn'
    r' e0 e1 e2 e3 e4
    (R': r' <5= rclo5 clo r)
    (CLOR': @cpn5 r' e0 e1 e2 e3 e4):
    @rclo5 clo r e0 e1 e2 e3 e4
.

Structure wcompatible5 (clo: rel -> rel) : Prop :=
  wcompat5_intro {
      wcompat5_mon: monotone5 clo;
      wcompat5_wcompat: forall r,
          clo (gf r) <5= gf (rclo5 clo r);
    }.

Lemma rclo5_mon_gen clo clo' r r' e0 e1 e2 e3 e4
      (IN: @rclo5 clo r e0 e1 e2 e3 e4)
      (LEclo: clo <6= clo')
      (LEr: r <5= r') :
  @rclo5 clo' r' e0 e1 e2 e3 e4.
Proof.
  induction IN; intros.
  - econstructor 1. apply LEr, R.
  - econstructor 2; [intros; eapply H, PR|apply LEclo, CLOR'].
  - econstructor 3; [intros; eapply H, PR|apply CLOR'].
  - econstructor 4; [intros; eapply H, PR|].
    eapply cpn5_mon; [apply CLOR'|].
    intros. apply PR.
Qed.

Lemma rclo5_mon clo:
  monotone5 (rclo5 clo).
Proof.
  repeat intro. eapply rclo5_mon_gen; [apply IN|intros; apply PR|apply LE].
Qed.

Lemma rclo5_clo clo r:
  clo (rclo5 clo r) <5= rclo5 clo r.
Proof.
  intros. econstructor 2; [|apply PR]. 
  intros. apply PR0.
Qed.

Lemma rclo5_step clo r:
  gf (rclo5 clo r) <5= rclo5 clo r.
Proof.
  intros. econstructor 3; [|apply PR].
  intros. apply PR0.
Qed.

Lemma rclo5_cpn clo r:
  cpn5 (rclo5 clo r) <5= rclo5 clo r.
Proof.
  intros. econstructor 4; [|apply PR]. 
  intros. apply PR0.
Qed.

Lemma rclo5_mult clo r:
  rclo5 clo (rclo5 clo r) <5= rclo5 clo r.
Proof.
  intros. induction PR.
  - eapply R.
  - econstructor 2; [eapply H | eapply CLOR'].
  - econstructor 3; [eapply H | eapply CLOR'].
  - econstructor 4; [eapply H | eapply CLOR'].
Qed.

Lemma rclo5_compose clo r:
  rclo5 (rclo5 clo) r <5= rclo5 clo r.
Proof.
  intros. induction PR.
  - apply rclo5_base, R.
  - apply rclo5_mult.
    eapply rclo5_mon; [apply CLOR'|apply H].
  - apply rclo5_step.
    eapply gf_mon; [apply CLOR'|apply H].
  - apply rclo5_cpn.
    eapply cpn5_mon; [apply CLOR'|apply H].
Qed.

Lemma wcompat5_compat
      clo (WCOM: wcompatible5 clo):
  compatible5 (rclo5 clo).
Proof.
  econstructor; [eapply rclo5_mon|]. intros.
  induction PR; intros.
  - eapply gf_mon; [apply R|]. intros.
    apply rclo5_base. apply PR.
  - eapply gf_mon.
    + eapply (wcompat5_wcompat WCOM).
      eapply (wcompat5_mon WCOM); [apply CLOR'|apply H].
    + intros. apply rclo5_mult, PR.
  - eapply gf_mon; [apply CLOR'|].
    intros. apply H in PR. apply rclo5_step, PR.
  - eapply gf_mon; [|intros; apply rclo5_cpn, PR].
    apply (compat5_compat cpn5_compat).
    eapply cpn5_mon; [apply CLOR'|apply H].
Qed.

Lemma wcompat5_sound clo (WCOM: wcompatible5 clo):
  clo <6= cpn5.
Proof.
  intros. exists (rclo5 clo).
  - apply wcompat5_compat, WCOM.
  - apply rclo5_clo.
    eapply (wcompat5_mon WCOM); [apply PR|].
    intros. apply rclo5_base, PR0.
Qed.

(** 
  Lemmas for tactics
*)

Lemma cpn5_base: forall r, r <5= cpn5 r.
Proof.
  intros. exists id.
  - econstructor; repeat intro.
    + apply LE, IN.
    + apply PR0.
  - apply PR.
Qed.

Lemma cpn5_from_upaco r:
  upaco5 gcpn5 r <5= cpn5 r.
Proof.
  intros. destruct PR; [| apply cpn5_base, H].
  exists (rclo5 (paco5 gcpn5)).
  - apply wcompat5_compat.
    econstructor; [apply paco5_mon|].
    intros. _punfold PR; [|apply gcpn5_mon].
    eapply gf_mon; [apply PR|].
    intros. apply rclo5_cpn.
    eapply cpn5_mon; [apply PR0|].
    intros. destruct PR1.
    + apply rclo5_clo.
      eapply paco5_mon; [apply H0|].
      intros. apply rclo5_step.
      eapply gf_mon; [apply PR1|].
      intros. apply rclo5_base, PR2.
    + apply rclo5_step.
      eapply gf_mon; [apply H0|].
      intros. apply rclo5_base, PR1.
  - apply rclo5_clo.
    eapply paco5_mon; [apply H|].
    intros. apply rclo5_base, PR.
Qed.

Lemma cpn5_from_paco r:
  paco5 gcpn5 r <5= cpn5 r.
Proof. intros. apply cpn5_from_upaco. left. apply PR. Qed.

Lemma gcpn5_from_paco r:
  paco5 gcpn5 r <5= gcpn5 r.
Proof.
  intros. _punfold PR; [|apply gcpn5_mon].
  eapply gf_mon; [apply PR|].
  intros. apply cpn5_comp.
  eapply cpn5_mon; [apply PR0|].
  apply cpn5_from_upaco.
Qed.

Lemma gcpn5_to_paco r:
  gcpn5 r <5= paco5 gcpn5 r.
Proof.
  intros. pfold. eapply gcpn5_mon; [apply PR|].
  intros. right. apply PR0.
Qed.  

Lemma cpn5_init:
  cpn5 bot5 <5= paco5 gf bot5.
Proof.
  intros. apply gcpn5_sound, gcpn5_to_paco, (compat5_compat cpn5_compat).
  eapply cpn5_mon; [apply PR|contradiction].
Qed.

Lemma cpn5_clo
      r clo (LE: clo <6= cpn5):
  clo (cpn5 r) <5= cpn5 r.
Proof.
  intros. apply cpn5_comp, LE, PR.
Qed.

Lemma gcpn5_clo
      r clo (LE: clo <6= cpn5):
  clo (gcpn5 r) <5= gcpn5 r.
Proof.
  intros. apply LE, (compat5_compat cpn5_compat) in PR.
  eapply gf_mon; [apply PR|].
  intros. apply cpn5_comp, PR0.
Qed.

Lemma cpn5_step r:
  gcpn5 r <5= cpn5 r.
Proof.
  intros. eapply cpn5_clo, PR.
  intros. eapply wcompat5_sound, PR0.
  econstructor; [apply gf_mon|].
  intros. eapply gf_mon; [apply PR1|].
  intros. apply rclo5_step.
  eapply gf_mon; [apply PR2|].
  intros. apply rclo5_base, PR3.
Qed.

Lemma cpn5_final: forall r, upaco5 gf r <5= cpn5 r.
Proof.
  intros. eapply cpn5_from_upaco.
  intros. eapply upaco5_mon_gen; [apply PR| |intros; apply PR0].
  intros. eapply gf_mon; [apply PR0|].
  intros. apply cpn5_base, PR1.
Qed.

Lemma gcpn5_final: forall r, paco5 gf r <5= gcpn5 r.
Proof.
  intros. _punfold PR; [|apply gf_mon].
  eapply gf_mon; [apply PR | apply cpn5_final].
Qed.

Lemma cpn5_complete:
  paco5 gf bot5 <5= cpn5 bot5.
Proof.
  intros. apply cpn5_from_paco.
  eapply paco5_mon_gen.
  - apply PR.
  - intros. eapply gf_mon; [apply PR0|apply cpn5_base].
  - intros. apply PR0.
Qed.

End Companion5.

Hint Resolve cpn5_base : paco.
Hint Resolve cpn5_mon : paco.
Hint Resolve gcpn5_mon : paco.
Hint Resolve rclo5_mon : paco.
Hint Resolve cpn5_final gcpn5_final : paco.

Hint Constructors cpn5 compatible5 wcompatible5.

Hint Constructors rclo5 : rclo.
Hint Resolve rclo5_clo rclo5_step rclo5_cpn : rclo.

