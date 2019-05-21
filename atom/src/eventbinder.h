/*-----------------------------------------------------------------------------
| Copyright (c) 2013-2017, Nucleic Development Team.
|
| Distributed under the terms of the Modified BSD License.
|
| The full license is in the file COPYING.txt, distributed with this software.
|----------------------------------------------------------------------------*/
#pragma once
#include "catom.h"
#include "member.h"


PyObject*
EventBinder_New( atom::Member* member, CAtom* atom );


int import_eventbinder();
