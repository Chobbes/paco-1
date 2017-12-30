from __future__ import print_function
import sys
from pacolib import *

if len(sys.argv) < 2: 
    sys.stderr.write('\nUsage: '+sys.argv[0]+' relsize\n\n') 
    sys.exit(1) 

relsize = int(sys.argv[1])

print ('Require Import JMeq.')
print ('Require Import hpattern.')
print ('Require Export paconotation.')
print ()
print ('(** * Tactic support for [paco] library')
print ()
print ('    This file defines tactics for converting the conclusion to the right form so')
print ('    that the accumulation lemmas can be usefully applied. These tactics are used')
print ('    in both internal and external approaches.')
print ()
print ('    Our main tactic, [pcofix], is defined at the end of the file and')
print ('    works for predicates of arity up to 14.')
print ('*)')
print ()
print ('(** ** Internal tactics *)')
print ()
print ('Inductive _paco_mark := _paco_mark_cons.')
print ()
print ('Inductive _paco_foo := _paco_foo_cons.')
print ()
print ('Definition _paco_id {A} (a : A) : A := a.')
print ()
print ('Lemma paco_eq_JMeq: forall A (a b: A), a = b -> _paco_id (JMeq a b).')
print ('Proof. intros; subst; apply JMeq_refl. Defined.')
print ()
print ('Lemma paco_JMeq_eq: forall (A : Type) (x y : A), _paco_id (JMeq x y) -> _paco_id (x = y).')
print ('Proof. intros; apply JMeq_eq; auto. Defined.')
print ()
print ('Ltac simplJM :=')
print ('  repeat match goal with [H: ?x |- _] =>')
print ('    match x with')
print ('    | _paco_id (JMeq _ _) => apply paco_JMeq_eq in H')
print ('    | _paco_id (?a = _) => unfold _paco_id in H; subst a')
print ('    end')
print ('  end.')
print ()
print ('Ltac hrewrite_last e H := let x := fresh "_paco_x_" in')
print ('  first [try (set (x:=e) at 17; fail 1);')
print ('    first [try (set (x:=e) at 9; fail 1);')
print ('      first [try (set (x:=e) at 5; fail 1);')
print ('        first [try (set (x:=e) at 3; fail 1);')
print ('          first [try (set (x:=e) at 2; fail 1);')
print ('            try (hrewrite H at 1)')
print ('          | try (hrewrite H at 2) ]')
print ('        | first [try (set (x:=e) at 4; fail 1);')
print ('            try (hrewrite H at 3)')
print ('          | try (hrewrite H at 4) ] ]')
print ('      | first [try (set (x:=e) at 7; fail 1);')
print ('          first [try (set (x:=e) at 6; fail 1);')
print ('            try (hrewrite H at 5)')
print ('          | try (hrewrite H at 6)]')
print ('        | first [try (set (x:=e) at 8; fail 1);')
print ('            try (hrewrite H at 7)')
print ('          | try (hrewrite H at 8) ] ] ]')
print ('    | first [try (set (x:=e) at 13; fail 1);')
print ('        first [try (set (x:=e) at 11; fail 1);')
print ('          first [try (set (x:=e) at 10; fail 1);')
print ('            try (hrewrite H at 9)')
print ('          | try (hrewrite H at 10) ]')
print ('        | first [try (set (x:=e) at 12; fail 1);')
print ('            try (hrewrite H at 11)')
print ('          | try (hrewrite H at 12) ] ]')
print ('      | first [try (set (x:=e) at 15; fail 1);')
print ('          first [try (set (x:=e) at 14; fail 1);')
print ('            try (hrewrite H at 13)')
print ('          | try (hrewrite H at 14)]')
print ('        | first [try (set (x:=e) at 16; fail 1);')
print ('            try (hrewrite H at 15)')
print ('          | try (hrewrite H at 16) ] ] ] ]')
print ('  | first [try (set (x:=e) at 25; fail 1);')
print ('      first [try (set (x:=e) at 21; fail 1);')
print ('        first [try (set (x:=e) at 19; fail 1);')
print ('          first [try (set (x:=e) at 18; fail 1);')
print ('            try (hrewrite H at 17)')
print ('          | try (hrewrite H at 18) ]')
print ('        | first [try (set (x:=e) at 20; fail 1);')
print ('            try (hrewrite H at 19)')
print ('          | try (hrewrite H at 20) ] ]')
print ('      | first [try (set (x:=e) at 23; fail 1);')
print ('          first [try (set (x:=e) at 22; fail 1);')
print ('            try (hrewrite H at 21)')
print ('          | try (hrewrite H at 22)]')
print ('        | first [try (set (x:=e) at 24; fail 1);')
print ('            try (hrewrite H at 23)')
print ('          | try (hrewrite H at 24) ] ] ]')
print ('    | first [try (set (x:=e) at 29; fail 1);')
print ('        first [try (set (x:=e) at 27; fail 1);')
print ('          first [try (set (x:=e) at 26; fail 1);')
print ('            try (hrewrite H at 25)')
print ('          | try (hrewrite H at 26) ]')
print ('        | first [try (set (x:=e) at 28; fail 1);')
print ('            try (hrewrite H at 27)')
print ('          | try (hrewrite H at 28) ] ]')
print ('      | first [try (set (x:=e) at 31; fail 1);')
print ('          first [try (set (x:=e) at 30; fail 1);')
print ('            try (hrewrite H at 29)')
print ('          | try (hrewrite H at 30)]')
print ('        | first [try (set (x:=e) at 32; fail 1);')
print ('            try (hrewrite H at 31)')
print ('          | try (hrewrite H at 32) ] ] ] ] ]')
print ('.')
print ()
print ('Ltac paco_generalize_hyp mark :=')
print ('  let y := fresh "_paco_rel_" in')
print ('  match goal with')
print ('  | [x: ?A |- _] =>')
print ('    match A with')
print ('    | mark => clear x')
print ('    | _ => intro y;')
print ('      match type of y with')
print ('        | context[x] => revert x y;')
print ('          match goal with [|-forall x, @?f x -> _] =>')
print ('            intros x y; generalize (ex_intro f x y)')
print ('          end')
print ('        | _ => generalize (conj (ex_intro _ x _paco_foo_cons) y)')
print ('      end; clear x y; paco_generalize_hyp mark')
print ('    end')
print ('  end.')
print ()
print ('Ltac paco_convert e x EQ :=')
print ('  generalize (eq_refl e); generalize e at 2; intros x EQ;')
print ('  hrewrite_last e EQ; apply eq_sym, paco_eq_JMeq in EQ; revert x EQ.')
print ()
print ('Ltac paco_destruct_hyp mark :=')
print ('  match goal with')
print ('  | [x: ?A |- _] =>')
print ('    match A with')
print ('    | mark => idtac')
print ('    | _paco_foo => clear x; paco_destruct_hyp mark')
print ("    | exists n, ?p => let n' := fresh n in destruct x as (n', x); paco_destruct_hyp mark")
print ("    | ?p /\ ?q => let x' := fresh x in destruct x as (x,x'); paco_destruct_hyp mark")
print ('    end')
print ('  end.')
print ()
print ('Ltac paco_revert_hyp mark :=')
print ('  match goal with [x: ?A |- _] =>')
print ('  match A with')
print ('    | mark => clear x')
print ('    | _ => revert x; paco_revert_hyp mark')
print ('  end end.')
print ()
print ('Ltac paco_post_var INC pr cr := let TMP := fresh "_paco_tmp_" in')
print ('  repeat (')
print ('    match goal with [H: context f [pr] |-_] =>')
print ('      let cih := context f [cr] in rename H into TMP;')
print ('      assert(H : cih) by (repeat intro; eapply INC, TMP; eassumption); clear TMP')
print ('    end);')
print ('  clear INC pr.')
print ()
print ('Ltac paco_rename_last :=')
print ('  let x := fresh "_paco_xxx_" in match goal with [H: _|-_] => rename H into x end.')
print ()
print ('Ltac paco_simp_hyp CIH :=')
print ('  let EP := fresh "_paco_EP_" in')
print ('  let FP := fresh "_paco_FF_" in')
print ('  let TP := fresh "_paco_TP_" in')
print ('  let XP := fresh "_paco_XP_" in')
print ('  let PP := type of CIH in')
print ('  evar (EP: Prop);')
print ('  assert (TP: False -> PP) by (')
print ('    intros FP; generalize _paco_mark_cons;')
print ('    repeat intro; paco_rename_last; paco_destruct_hyp _paco_mark;')
print ('    simplJM; paco_revert_hyp _paco_mark;')
print ('    let con := get_concl in set (TP:=con); revert EP; instantiate (1:= con); destruct FP);')
print ('  clear TP;')
print ('  assert (XP: EP) by (unfold EP; clear -CIH; repeat intro; apply CIH;')
print ('    first [')
print ('      (repeat match goal with | [ |- @ex _ _ ] => eexists | [ |- _ /\ _ ] => split end;')
print ('       try (apply paco_eq_JMeq; reflexivity);')
print ('       first [eassumption|apply _paco_foo_cons]); fail')
print ('    | (repeat match goal with | [ |- @ex _ _ ] => eexists | [ |- _ /\ _ ] => split end;')
print ('       eauto using paco_eq_JMeq, _paco_foo_cons)]);')
print ('  unfold EP in *; clear EP CIH; rename XP into CIH.')
print ()
print ('Ltac paco_post_simp CIH :=')
print ('  let CIH := fresh CIH in let TMP := fresh "_paco_TMP_" in')
print ('  intro CIH; paco_simp_hyp CIH;')
print ('  generalize _paco_mark_cons; intro TMP;')
print ('  repeat intro; paco_rename_last; paco_destruct_hyp _paco_mark;')
print ('  simplJM; paco_revert_hyp _paco_mark.')
print ()
print ('Ltac paco_ren_r nr cr :=')
print ('  first [rename cr into nr | let nr := fresh nr in rename cr into nr].')
print ()
print ('Ltac paco_ren_pr pr cr := rename cr into pr.')
print ()
print ('Ltac paco_revert :=')
print ('  match goal with [H: _ |- _] => revert H end.')
print ('')
print ('Ltac paco_cofix_auto :=')
print ('  cofix; repeat intro;')
print ('  match goal with [H: _ |- _] => destruct H end; econstructor;')
print ('  try (match goal with [H: _|-_] => apply H end); intros;')
print ('  lazymatch goal with [PR: _ |- _] => match goal with [H: _ |- _] => apply H in PR end end;')
print ('  repeat match goal with [ H : _ \/ _ |- _] => destruct H end; first [eauto; fail|eauto 10].')
print ('')

print ('(** *** Arity 0')
print ('*)')
print ()
print ('Ltac paco_cont0 :=')
print ('generalize _paco_foo_cons; paco_generalize_hyp _paco_mark.')
print ()
print ('Ltac paco_pre0 :=')
print ('generalize _paco_mark_cons; repeat intro; paco_cont0.')
print ()
print ('Ltac paco_post_match0 INC tac1 tac2 :=')
print ('let cr := fresh "_paco_cr_" in intros cr INC; repeat (red in INC);')
print ('match goal with [H: ?x |- _] => match x with')
print ('| (pacoid _) -> _ => clear H; tac1 cr')
print ('| ?pr -> _ => paco_post_var INC pr cr; tac2 pr cr')
print ('| _ => tac1 cr')
print ('end end.')
print ()
print ('Tactic Notation "paco_post0" ident(CIH) "with" ident(nr) :=')
print ('let INC := fresh "_paco_inc_" in')
print ('paco_post_match0 INC ltac:(paco_ren_r nr) paco_ren_pr; paco_post_simp CIH;')
print ("let CIH' := fresh CIH in try rename INC into CIH'.")
print ()

for n in range (1,relsize+1):
    print ("(** *** Arity "+str(n)) 
    print ("*)")
    print ()
    print ("Ltac paco_cont"+str(n)+itrstr(" e",n)+" := ")
    for i in range(n):
        print ('let x'+str(i)+' := fresh "_paco_v_" in let EQ'+str(i)+' := fresh "_paco_EQ_" in')
    for i in reversed(range(n)):
        print ('paco_convert e'+str(i)+' x'+str(i)+' EQ'+str(i)+';')
    for i in range(n):
        print ('intros x'+str(i)+' EQ'+str(i)+';')
    print ('generalize'+itrstr(' (conj EQ',n-1)+' EQ'+str(n-1)+(n-1)*')'+'; clear'+itrstr(' EQ',n)+';')
    print (itrstr('move x',n,' at top; '))
    print ('paco_generalize_hyp _paco_mark; revert'+itrstr(' x',n)+'.')
    print ()

    print ('Lemma _paco_pre'+str(n)+': forall'+itrstr(' T',n)+' (gf: rel'+str(n)+itrstr(' T',n)+')'+itrstr(' x',n))
    print ("(X: let gf' := gf in gf'"+itrstr(" x",n)+"), gf"+itrstr(" x",n)+".")
    print ('Proof. intros; apply X. Defined.')
    print ()

    print ('Ltac paco_pre'+str(n)+' := let X := fresh "_paco_X_" in')
    print ('generalize _paco_mark_cons; repeat intro;')
    print ('apply _paco_pre'+str(n)+'; intro X;')
    print ('match goal with')
    print ('| |- _'+itrstr(' ?e',n)+' => unfold X; clear X; paco_cont'+str(n)+itrstr(' e',n))
    print ('end.')
    print ()

    print ('Ltac paco_post_match'+str(n)+' INC tac1 tac2 :=')
    print ('let cr := fresh "_paco_cr_" in intros cr INC; repeat (red in INC);')
    print ('match goal with [H: ?x |- _] => match x with')
    print ('| forall'+n*' _'+', (pacoid _)'+n*' _'+' -> _ => clear H; tac1 cr')
    print ('| forall'+n*' _'+', ?pr'+n*' _'+' -> _ => paco_post_var INC pr cr; tac2 pr cr')
    print ('| _ => tac1 cr')
    print ('end end.')
    print ()

    print ('Tactic Notation "paco_post'+str(n)+'" ident(CIH) "with" ident(nr) :=')
    print ('let INC := fresh "_paco_inc_" in')
    print ('paco_post_match'+str(n)+' INC ltac:(paco_ren_r nr) paco_ren_pr; paco_post_simp CIH;')
    print ("let CIH' := fresh CIH in try rename INC into CIH'.")
    print ()

print ("(** ** External interface *)")
print ()
print ("(** We provide our main tactics:")
print ()
print ("    - [pcofix{n} ident using lemma with ident']")
print ()
print ()
print ("    where [ident] is the identifier used to name the generated coinduction hypothesis,")
print ("    [lemma] is an expression denoting which accumulation lemma is to be used, and")
print ("    [ident'] is the identifier used to name the accumulation variable.")
print ("*)")
print ()

for n in range(relsize+1):
    print ('Tactic Notation "pcofix'+str(n)+'" ident(CIH) "using" constr(lem) "with" ident(r) :=')
    print ('paco_pre'+str(n)+'; eapply lem; paco_post'+str(n)+' CIH with r.')
    print ()

print ('(** [pcofix] automatically figures out the appropriate index [n] from')
print ('    the type of the accumulation lemma [lem] and applies [pcofix{n}].')
print ('*)')
print ()

print ('Tactic Notation "pcofix" ident(CIH) "using" constr(lem) "with" ident(nr) :=')
print ('  let N := fresh "_paco_N_" in let TMP := fresh "_paco_TMP_" in')
print ('  evar (N : nat);')
print ('  let P := type of lem in')
print ('  assert (TMP: False -> P) by')
print ('    (intro TMP; repeat intro; match goal with [H : _ |- _] => revert H end;')
print ('     match goal with')
for n in reversed(range(relsize+1)):
    print ('     | [|- _'+n*' _'+' -> _] => revert N; instantiate (1 := '+str(n)+')')
print ('     end; destruct TMP);')
print ('  clear TMP;')
print ('  revert N;')
print ('  match goal with ')
for n in range(relsize+1):
    print ('  | [|- let _ := '+str(n)+' in _] => intros _; pcofix'+str(n)+' CIH using lem with nr')
print ('  end.')
print ()

print ('Tactic Notation "pcofix" ident(CIH) "using" constr(lem) :=') 
print ('  pcofix CIH using lem with r.')
print ()

