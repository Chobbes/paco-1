Require Export paconotation pacotacuser.
Require Import pacotac.
Set Implicit Arguments.

(** ** Predicates of Arity 3
*)

Section Arg3_def.
Variable T0 : Type.
Variable T1 : forall (x0: @T0), Type.
Variable T2 : forall (x0: @T0) (x1: @T1 x0), Type.
Variable gf : rel3 T0 T1 T2 -> rel3 T0 T1 T2.
Implicit Arguments gf [].

CoInductive paco3( r: rel3 T0 T1 T2) x0 x1 x2 : Prop :=
| paco3_pfold pco
    (LE : pco <3= (paco3 r \3/ r))
    (SIM: gf pco x0 x1 x2)
.
Definition upaco3( r: rel3 T0 T1 T2) := paco3 r \3/ r.
End Arg3_def.
Implicit Arguments paco3 [ T0 T1 T2 ].
Implicit Arguments upaco3 [ T0 T1 T2 ].
Hint Unfold upaco3.

Section Arg3_2_def.
Variable T0 : Type.
Variable T1 : forall (x0: @T0), Type.
Variable T2 : forall (x0: @T0) (x1: @T1 x0), Type.
Variable gf_0 gf_1 : rel3 T0 T1 T2 -> rel3 T0 T1 T2 -> rel3 T0 T1 T2.
Implicit Arguments gf_0 [].
Implicit Arguments gf_1 [].

CoInductive paco3_2_0( r_0 r_1: rel3 T0 T1 T2) x0 x1 x2 : Prop :=
| paco3_2_0_pfold pco_0 pco_1
    (LE : pco_0 <3= (paco3_2_0 r_0 r_1 \3/ r_0))
    (LE : pco_1 <3= (paco3_2_1 r_0 r_1 \3/ r_1))
    (SIM: gf_0 pco_0 pco_1 x0 x1 x2)
with paco3_2_1( r_0 r_1: rel3 T0 T1 T2) x0 x1 x2 : Prop :=
| paco3_2_1_pfold pco_0 pco_1
    (LE : pco_0 <3= (paco3_2_0 r_0 r_1 \3/ r_0))
    (LE : pco_1 <3= (paco3_2_1 r_0 r_1 \3/ r_1))
    (SIM: gf_1 pco_0 pco_1 x0 x1 x2)
.
Definition upaco3_2_0( r_0 r_1: rel3 T0 T1 T2) := paco3_2_0 r_0 r_1 \3/ r_0.
Definition upaco3_2_1( r_0 r_1: rel3 T0 T1 T2) := paco3_2_1 r_0 r_1 \3/ r_1.
End Arg3_2_def.
Implicit Arguments paco3_2_0 [ T0 T1 T2 ].
Implicit Arguments upaco3_2_0 [ T0 T1 T2 ].
Hint Unfold upaco3_2_0.
Implicit Arguments paco3_2_1 [ T0 T1 T2 ].
Implicit Arguments upaco3_2_1 [ T0 T1 T2 ].
Hint Unfold upaco3_2_1.

Section Arg3_3_def.
Variable T0 : Type.
Variable T1 : forall (x0: @T0), Type.
Variable T2 : forall (x0: @T0) (x1: @T1 x0), Type.
Variable gf_0 gf_1 gf_2 : rel3 T0 T1 T2 -> rel3 T0 T1 T2 -> rel3 T0 T1 T2 -> rel3 T0 T1 T2.
Implicit Arguments gf_0 [].
Implicit Arguments gf_1 [].
Implicit Arguments gf_2 [].

CoInductive paco3_3_0( r_0 r_1 r_2: rel3 T0 T1 T2) x0 x1 x2 : Prop :=
| paco3_3_0_pfold pco_0 pco_1 pco_2
    (LE : pco_0 <3= (paco3_3_0 r_0 r_1 r_2 \3/ r_0))
    (LE : pco_1 <3= (paco3_3_1 r_0 r_1 r_2 \3/ r_1))
    (LE : pco_2 <3= (paco3_3_2 r_0 r_1 r_2 \3/ r_2))
    (SIM: gf_0 pco_0 pco_1 pco_2 x0 x1 x2)
with paco3_3_1( r_0 r_1 r_2: rel3 T0 T1 T2) x0 x1 x2 : Prop :=
| paco3_3_1_pfold pco_0 pco_1 pco_2
    (LE : pco_0 <3= (paco3_3_0 r_0 r_1 r_2 \3/ r_0))
    (LE : pco_1 <3= (paco3_3_1 r_0 r_1 r_2 \3/ r_1))
    (LE : pco_2 <3= (paco3_3_2 r_0 r_1 r_2 \3/ r_2))
    (SIM: gf_1 pco_0 pco_1 pco_2 x0 x1 x2)
with paco3_3_2( r_0 r_1 r_2: rel3 T0 T1 T2) x0 x1 x2 : Prop :=
| paco3_3_2_pfold pco_0 pco_1 pco_2
    (LE : pco_0 <3= (paco3_3_0 r_0 r_1 r_2 \3/ r_0))
    (LE : pco_1 <3= (paco3_3_1 r_0 r_1 r_2 \3/ r_1))
    (LE : pco_2 <3= (paco3_3_2 r_0 r_1 r_2 \3/ r_2))
    (SIM: gf_2 pco_0 pco_1 pco_2 x0 x1 x2)
.
Definition upaco3_3_0( r_0 r_1 r_2: rel3 T0 T1 T2) := paco3_3_0 r_0 r_1 r_2 \3/ r_0.
Definition upaco3_3_1( r_0 r_1 r_2: rel3 T0 T1 T2) := paco3_3_1 r_0 r_1 r_2 \3/ r_1.
Definition upaco3_3_2( r_0 r_1 r_2: rel3 T0 T1 T2) := paco3_3_2 r_0 r_1 r_2 \3/ r_2.
End Arg3_3_def.
Implicit Arguments paco3_3_0 [ T0 T1 T2 ].
Implicit Arguments upaco3_3_0 [ T0 T1 T2 ].
Hint Unfold upaco3_3_0.
Implicit Arguments paco3_3_1 [ T0 T1 T2 ].
Implicit Arguments upaco3_3_1 [ T0 T1 T2 ].
Hint Unfold upaco3_3_1.
Implicit Arguments paco3_3_2 [ T0 T1 T2 ].
Implicit Arguments upaco3_3_2 [ T0 T1 T2 ].
Hint Unfold upaco3_3_2.

(* Less than or equal - internal use only *)
Notation "p <_paco_3= q" :=
  (forall _paco_x0 _paco_x1 _paco_x2 (PR: p _paco_x0 _paco_x1 _paco_x2 : Prop), q _paco_x0 _paco_x1 _paco_x2 : Prop)
  (at level 50, no associativity).

(** 1 Mutual Coinduction *)

Section Arg3_1.

Definition monotone3 T0 T1 T2 (gf: rel3 T0 T1 T2 -> rel3 T0 T1 T2) :=
  forall x0 x1 x2 r r' (IN: gf r x0 x1 x2) (LE: r <3= r'), gf r' x0 x1 x2.

Variable T0 : Type.
Variable T1 : forall (x0: @T0), Type.
Variable T2 : forall (x0: @T0) (x1: @T1 x0), Type.
Variable gf : rel3 T0 T1 T2 -> rel3 T0 T1 T2.
Implicit Arguments gf [].

Theorem paco3_acc: forall
  l r (OBG: forall rr (INC: r <3= rr) (CIH: l <_paco_3= rr), l <_paco_3= paco3 gf rr),
  l <3= paco3 gf r.
Proof.
  intros; assert (SIM: paco3 gf (r \3/ l) x0 x1 x2) by eauto.
  clear PR; repeat (try left; do 4 paco_revert; paco_cofix_auto).
Qed.

Theorem paco3_mon: monotone3 (paco3 gf).
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Theorem paco3_mult_strong: forall r,
  paco3 gf (upaco3 gf r) <3= paco3 gf r.
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Corollary paco3_mult: forall r,
  paco3 gf (paco3 gf r) <3= paco3 gf r.
Proof. intros; eapply paco3_mult_strong, paco3_mon; eauto. Qed.

Theorem paco3_fold: forall r,
  gf (upaco3 gf r) <3= paco3 gf r.
Proof. intros; econstructor; [ |eauto]; eauto. Qed.

Theorem paco3_unfold: forall (MON: monotone3 gf) r,
  paco3 gf r <3= gf (upaco3 gf r).
Proof. unfold monotone3; intros; destruct PR; eauto. Qed.

End Arg3_1.

Hint Unfold monotone3.
Hint Resolve paco3_fold.

Implicit Arguments paco3_acc            [ T0 T1 T2 ].
Implicit Arguments paco3_mon            [ T0 T1 T2 ].
Implicit Arguments paco3_mult_strong    [ T0 T1 T2 ].
Implicit Arguments paco3_mult           [ T0 T1 T2 ].
Implicit Arguments paco3_fold           [ T0 T1 T2 ].
Implicit Arguments paco3_unfold         [ T0 T1 T2 ].

Instance paco3_inst  T0 T1 T2 (gf : rel3 T0 T1 T2->_) r x0 x1 x2 : paco_class (paco3 gf r x0 x1 x2) :=
{ pacoacc    := paco3_acc gf;
  pacomult   := paco3_mult gf;
  pacofold   := paco3_fold gf;
  pacounfold := paco3_unfold gf }.

(** 2 Mutual Coinduction *)

Section Arg3_2.

Definition monotone3_2 T0 T1 T2 (gf: rel3 T0 T1 T2 -> rel3 T0 T1 T2 -> rel3 T0 T1 T2) :=
  forall x0 x1 x2 r_0 r_1 r'_0 r'_1 (IN: gf r_0 r_1 x0 x1 x2) (LE_0: r_0 <3= r'_0)(LE_1: r_1 <3= r'_1), gf r'_0 r'_1 x0 x1 x2.

Variable T0 : Type.
Variable T1 : forall (x0: @T0), Type.
Variable T2 : forall (x0: @T0) (x1: @T1 x0), Type.
Variable gf_0 gf_1 : rel3 T0 T1 T2 -> rel3 T0 T1 T2 -> rel3 T0 T1 T2.
Implicit Arguments gf_0 [].
Implicit Arguments gf_1 [].

Theorem paco3_2_0_acc: forall
  l r_0 r_1 (OBG: forall rr (INC: r_0 <3= rr) (CIH: l <_paco_3= rr), l <_paco_3= paco3_2_0 gf_0 gf_1 rr r_1),
  l <3= paco3_2_0 gf_0 gf_1 r_0 r_1.
Proof.
  intros; assert (SIM: paco3_2_0 gf_0 gf_1 (r_0 \3/ l) r_1 x0 x1 x2) by eauto.
  clear PR; repeat (try left; do 4 paco_revert; paco_cofix_auto).
Qed.

Theorem paco3_2_1_acc: forall
  l r_0 r_1 (OBG: forall rr (INC: r_1 <3= rr) (CIH: l <_paco_3= rr), l <_paco_3= paco3_2_1 gf_0 gf_1 r_0 rr),
  l <3= paco3_2_1 gf_0 gf_1 r_0 r_1.
Proof.
  intros; assert (SIM: paco3_2_1 gf_0 gf_1 r_0 (r_1 \3/ l) x0 x1 x2) by eauto.
  clear PR; repeat (try left; do 4 paco_revert; paco_cofix_auto).
Qed.

Theorem paco3_2_0_mon: monotone3_2 (paco3_2_0 gf_0 gf_1).
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Theorem paco3_2_1_mon: monotone3_2 (paco3_2_1 gf_0 gf_1).
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Theorem paco3_2_0_mult_strong: forall r_0 r_1,
  paco3_2_0 gf_0 gf_1 (upaco3_2_0 gf_0 gf_1 r_0 r_1) (upaco3_2_1 gf_0 gf_1 r_0 r_1) <3= paco3_2_0 gf_0 gf_1 r_0 r_1.
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Theorem paco3_2_1_mult_strong: forall r_0 r_1,
  paco3_2_1 gf_0 gf_1 (upaco3_2_0 gf_0 gf_1 r_0 r_1) (upaco3_2_1 gf_0 gf_1 r_0 r_1) <3= paco3_2_1 gf_0 gf_1 r_0 r_1.
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Corollary paco3_2_0_mult: forall r_0 r_1,
  paco3_2_0 gf_0 gf_1 (paco3_2_0 gf_0 gf_1 r_0 r_1) (paco3_2_1 gf_0 gf_1 r_0 r_1) <3= paco3_2_0 gf_0 gf_1 r_0 r_1.
Proof. intros; eapply paco3_2_0_mult_strong, paco3_2_0_mon; eauto. Qed.

Corollary paco3_2_1_mult: forall r_0 r_1,
  paco3_2_1 gf_0 gf_1 (paco3_2_0 gf_0 gf_1 r_0 r_1) (paco3_2_1 gf_0 gf_1 r_0 r_1) <3= paco3_2_1 gf_0 gf_1 r_0 r_1.
Proof. intros; eapply paco3_2_1_mult_strong, paco3_2_1_mon; eauto. Qed.

Theorem paco3_2_0_fold: forall r_0 r_1,
  gf_0 (upaco3_2_0 gf_0 gf_1 r_0 r_1) (upaco3_2_1 gf_0 gf_1 r_0 r_1) <3= paco3_2_0 gf_0 gf_1 r_0 r_1.
Proof. intros; econstructor; [ | |eauto]; eauto. Qed.

Theorem paco3_2_1_fold: forall r_0 r_1,
  gf_1 (upaco3_2_0 gf_0 gf_1 r_0 r_1) (upaco3_2_1 gf_0 gf_1 r_0 r_1) <3= paco3_2_1 gf_0 gf_1 r_0 r_1.
Proof. intros; econstructor; [ | |eauto]; eauto. Qed.

Theorem paco3_2_0_unfold: forall (MON: monotone3_2 gf_0) (MON: monotone3_2 gf_1) r_0 r_1,
  paco3_2_0 gf_0 gf_1 r_0 r_1 <3= gf_0 (upaco3_2_0 gf_0 gf_1 r_0 r_1) (upaco3_2_1 gf_0 gf_1 r_0 r_1).
Proof. unfold monotone3_2; intros; destruct PR; eauto. Qed.

Theorem paco3_2_1_unfold: forall (MON: monotone3_2 gf_0) (MON: monotone3_2 gf_1) r_0 r_1,
  paco3_2_1 gf_0 gf_1 r_0 r_1 <3= gf_1 (upaco3_2_0 gf_0 gf_1 r_0 r_1) (upaco3_2_1 gf_0 gf_1 r_0 r_1).
Proof. unfold monotone3_2; intros; destruct PR; eauto. Qed.

End Arg3_2.

Hint Unfold monotone3_2.
Hint Resolve paco3_2_0_fold.
Hint Resolve paco3_2_1_fold.

Implicit Arguments paco3_2_0_acc            [ T0 T1 T2 ].
Implicit Arguments paco3_2_1_acc            [ T0 T1 T2 ].
Implicit Arguments paco3_2_0_mon            [ T0 T1 T2 ].
Implicit Arguments paco3_2_1_mon            [ T0 T1 T2 ].
Implicit Arguments paco3_2_0_mult_strong    [ T0 T1 T2 ].
Implicit Arguments paco3_2_1_mult_strong    [ T0 T1 T2 ].
Implicit Arguments paco3_2_0_mult           [ T0 T1 T2 ].
Implicit Arguments paco3_2_1_mult           [ T0 T1 T2 ].
Implicit Arguments paco3_2_0_fold           [ T0 T1 T2 ].
Implicit Arguments paco3_2_1_fold           [ T0 T1 T2 ].
Implicit Arguments paco3_2_0_unfold         [ T0 T1 T2 ].
Implicit Arguments paco3_2_1_unfold         [ T0 T1 T2 ].

Instance paco3_2_0_inst  T0 T1 T2 (gf_0 gf_1 : rel3 T0 T1 T2->_) r_0 r_1 x0 x1 x2 : paco_class (paco3_2_0 gf_0 gf_1 r_0 r_1 x0 x1 x2) :=
{ pacoacc    := paco3_2_0_acc gf_0 gf_1;
  pacomult   := paco3_2_0_mult gf_0 gf_1;
  pacofold   := paco3_2_0_fold gf_0 gf_1;
  pacounfold := paco3_2_0_unfold gf_0 gf_1 }.

Instance paco3_2_1_inst  T0 T1 T2 (gf_0 gf_1 : rel3 T0 T1 T2->_) r_0 r_1 x0 x1 x2 : paco_class (paco3_2_1 gf_0 gf_1 r_0 r_1 x0 x1 x2) :=
{ pacoacc    := paco3_2_1_acc gf_0 gf_1;
  pacomult   := paco3_2_1_mult gf_0 gf_1;
  pacofold   := paco3_2_1_fold gf_0 gf_1;
  pacounfold := paco3_2_1_unfold gf_0 gf_1 }.

(** 3 Mutual Coinduction *)

Section Arg3_3.

Definition monotone3_3 T0 T1 T2 (gf: rel3 T0 T1 T2 -> rel3 T0 T1 T2 -> rel3 T0 T1 T2 -> rel3 T0 T1 T2) :=
  forall x0 x1 x2 r_0 r_1 r_2 r'_0 r'_1 r'_2 (IN: gf r_0 r_1 r_2 x0 x1 x2) (LE_0: r_0 <3= r'_0)(LE_1: r_1 <3= r'_1)(LE_2: r_2 <3= r'_2), gf r'_0 r'_1 r'_2 x0 x1 x2.

Variable T0 : Type.
Variable T1 : forall (x0: @T0), Type.
Variable T2 : forall (x0: @T0) (x1: @T1 x0), Type.
Variable gf_0 gf_1 gf_2 : rel3 T0 T1 T2 -> rel3 T0 T1 T2 -> rel3 T0 T1 T2 -> rel3 T0 T1 T2.
Implicit Arguments gf_0 [].
Implicit Arguments gf_1 [].
Implicit Arguments gf_2 [].

Theorem paco3_3_0_acc: forall
  l r_0 r_1 r_2 (OBG: forall rr (INC: r_0 <3= rr) (CIH: l <_paco_3= rr), l <_paco_3= paco3_3_0 gf_0 gf_1 gf_2 rr r_1 r_2),
  l <3= paco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof.
  intros; assert (SIM: paco3_3_0 gf_0 gf_1 gf_2 (r_0 \3/ l) r_1 r_2 x0 x1 x2) by eauto.
  clear PR; repeat (try left; do 4 paco_revert; paco_cofix_auto).
Qed.

Theorem paco3_3_1_acc: forall
  l r_0 r_1 r_2 (OBG: forall rr (INC: r_1 <3= rr) (CIH: l <_paco_3= rr), l <_paco_3= paco3_3_1 gf_0 gf_1 gf_2 r_0 rr r_2),
  l <3= paco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof.
  intros; assert (SIM: paco3_3_1 gf_0 gf_1 gf_2 r_0 (r_1 \3/ l) r_2 x0 x1 x2) by eauto.
  clear PR; repeat (try left; do 4 paco_revert; paco_cofix_auto).
Qed.

Theorem paco3_3_2_acc: forall
  l r_0 r_1 r_2 (OBG: forall rr (INC: r_2 <3= rr) (CIH: l <_paco_3= rr), l <_paco_3= paco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 rr),
  l <3= paco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof.
  intros; assert (SIM: paco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 (r_2 \3/ l) x0 x1 x2) by eauto.
  clear PR; repeat (try left; do 4 paco_revert; paco_cofix_auto).
Qed.

Theorem paco3_3_0_mon: monotone3_3 (paco3_3_0 gf_0 gf_1 gf_2).
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Theorem paco3_3_1_mon: monotone3_3 (paco3_3_1 gf_0 gf_1 gf_2).
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Theorem paco3_3_2_mon: monotone3_3 (paco3_3_2 gf_0 gf_1 gf_2).
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Theorem paco3_3_0_mult_strong: forall r_0 r_1 r_2,
  paco3_3_0 gf_0 gf_1 gf_2 (upaco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2) <3= paco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Theorem paco3_3_1_mult_strong: forall r_0 r_1 r_2,
  paco3_3_1 gf_0 gf_1 gf_2 (upaco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2) <3= paco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Theorem paco3_3_2_mult_strong: forall r_0 r_1 r_2,
  paco3_3_2 gf_0 gf_1 gf_2 (upaco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2) <3= paco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof. paco_cofix_auto; repeat (left; do 4 paco_revert; paco_cofix_auto). Qed.

Corollary paco3_3_0_mult: forall r_0 r_1 r_2,
  paco3_3_0 gf_0 gf_1 gf_2 (paco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (paco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (paco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2) <3= paco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof. intros; eapply paco3_3_0_mult_strong, paco3_3_0_mon; eauto. Qed.

Corollary paco3_3_1_mult: forall r_0 r_1 r_2,
  paco3_3_1 gf_0 gf_1 gf_2 (paco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (paco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (paco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2) <3= paco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof. intros; eapply paco3_3_1_mult_strong, paco3_3_1_mon; eauto. Qed.

Corollary paco3_3_2_mult: forall r_0 r_1 r_2,
  paco3_3_2 gf_0 gf_1 gf_2 (paco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (paco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (paco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2) <3= paco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof. intros; eapply paco3_3_2_mult_strong, paco3_3_2_mon; eauto. Qed.

Theorem paco3_3_0_fold: forall r_0 r_1 r_2,
  gf_0 (upaco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2) <3= paco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof. intros; econstructor; [ | | |eauto]; eauto. Qed.

Theorem paco3_3_1_fold: forall r_0 r_1 r_2,
  gf_1 (upaco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2) <3= paco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof. intros; econstructor; [ | | |eauto]; eauto. Qed.

Theorem paco3_3_2_fold: forall r_0 r_1 r_2,
  gf_2 (upaco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2) <3= paco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2.
Proof. intros; econstructor; [ | | |eauto]; eauto. Qed.

Theorem paco3_3_0_unfold: forall (MON: monotone3_3 gf_0) (MON: monotone3_3 gf_1) (MON: monotone3_3 gf_2) r_0 r_1 r_2,
  paco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2 <3= gf_0 (upaco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2).
Proof. unfold monotone3_3; intros; destruct PR; eauto. Qed.

Theorem paco3_3_1_unfold: forall (MON: monotone3_3 gf_0) (MON: monotone3_3 gf_1) (MON: monotone3_3 gf_2) r_0 r_1 r_2,
  paco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2 <3= gf_1 (upaco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2).
Proof. unfold monotone3_3; intros; destruct PR; eauto. Qed.

Theorem paco3_3_2_unfold: forall (MON: monotone3_3 gf_0) (MON: monotone3_3 gf_1) (MON: monotone3_3 gf_2) r_0 r_1 r_2,
  paco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2 <3= gf_2 (upaco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2) (upaco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2).
Proof. unfold monotone3_3; intros; destruct PR; eauto. Qed.

End Arg3_3.

Hint Unfold monotone3_3.
Hint Resolve paco3_3_0_fold.
Hint Resolve paco3_3_1_fold.
Hint Resolve paco3_3_2_fold.

Implicit Arguments paco3_3_0_acc            [ T0 T1 T2 ].
Implicit Arguments paco3_3_1_acc            [ T0 T1 T2 ].
Implicit Arguments paco3_3_2_acc            [ T0 T1 T2 ].
Implicit Arguments paco3_3_0_mon            [ T0 T1 T2 ].
Implicit Arguments paco3_3_1_mon            [ T0 T1 T2 ].
Implicit Arguments paco3_3_2_mon            [ T0 T1 T2 ].
Implicit Arguments paco3_3_0_mult_strong    [ T0 T1 T2 ].
Implicit Arguments paco3_3_1_mult_strong    [ T0 T1 T2 ].
Implicit Arguments paco3_3_2_mult_strong    [ T0 T1 T2 ].
Implicit Arguments paco3_3_0_mult           [ T0 T1 T2 ].
Implicit Arguments paco3_3_1_mult           [ T0 T1 T2 ].
Implicit Arguments paco3_3_2_mult           [ T0 T1 T2 ].
Implicit Arguments paco3_3_0_fold           [ T0 T1 T2 ].
Implicit Arguments paco3_3_1_fold           [ T0 T1 T2 ].
Implicit Arguments paco3_3_2_fold           [ T0 T1 T2 ].
Implicit Arguments paco3_3_0_unfold         [ T0 T1 T2 ].
Implicit Arguments paco3_3_1_unfold         [ T0 T1 T2 ].
Implicit Arguments paco3_3_2_unfold         [ T0 T1 T2 ].

Instance paco3_3_0_inst  T0 T1 T2 (gf_0 gf_1 gf_2 : rel3 T0 T1 T2->_) r_0 r_1 r_2 x0 x1 x2 : paco_class (paco3_3_0 gf_0 gf_1 gf_2 r_0 r_1 r_2 x0 x1 x2) :=
{ pacoacc    := paco3_3_0_acc gf_0 gf_1 gf_2;
  pacomult   := paco3_3_0_mult gf_0 gf_1 gf_2;
  pacofold   := paco3_3_0_fold gf_0 gf_1 gf_2;
  pacounfold := paco3_3_0_unfold gf_0 gf_1 gf_2 }.

Instance paco3_3_1_inst  T0 T1 T2 (gf_0 gf_1 gf_2 : rel3 T0 T1 T2->_) r_0 r_1 r_2 x0 x1 x2 : paco_class (paco3_3_1 gf_0 gf_1 gf_2 r_0 r_1 r_2 x0 x1 x2) :=
{ pacoacc    := paco3_3_1_acc gf_0 gf_1 gf_2;
  pacomult   := paco3_3_1_mult gf_0 gf_1 gf_2;
  pacofold   := paco3_3_1_fold gf_0 gf_1 gf_2;
  pacounfold := paco3_3_1_unfold gf_0 gf_1 gf_2 }.

Instance paco3_3_2_inst  T0 T1 T2 (gf_0 gf_1 gf_2 : rel3 T0 T1 T2->_) r_0 r_1 r_2 x0 x1 x2 : paco_class (paco3_3_2 gf_0 gf_1 gf_2 r_0 r_1 r_2 x0 x1 x2) :=
{ pacoacc    := paco3_3_2_acc gf_0 gf_1 gf_2;
  pacomult   := paco3_3_2_mult gf_0 gf_1 gf_2;
  pacofold   := paco3_3_2_fold gf_0 gf_1 gf_2;
  pacounfold := paco3_3_2_unfold gf_0 gf_1 gf_2 }.

