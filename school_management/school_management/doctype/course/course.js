// Copyright (c) 2022, Advintic and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Course", {
// 	refresh(frm) {

// 	},
// });

//frappe.ui.form.on('Enrolled Students', 'validate', function(frm, cdt, cdn){ // The child table is defined in a DoctType called "Enrolled Students"
//
//        console.log("Hi")
//        if(frm.level==cdt.student_level){
//            console.log("Herrrr")
//
//        }else{
//        console.log("Not equaal")
//             frappe.msgprint('Student Level SHould be the same as the course level! ');
//            return false
//
//    }
//});

//frappe.ui.form.on("Enrolled Students", "validate", function(frm, cdt, cdn) {
//    console.log("Hi")
////	$.each(frm.doc.items || [], function(i, d) {
////		if(d.customized == "Yes" && !d.standard_customization) {
////			frappe.throw("Standard Customization is mandatory");
////		}
////	})
//});




//frappe.ui.form.on('Enrolled Students', { // The child table is defined in a DoctType called "Dynamic Link"
//    enrolled_students_add(frm, cdt, cdn) { // "links" is the name of the table field i
//        // frm: curren
//        // cdt: child DocType 'Dynamic Link'
//        // cdn: child docname (something like 'a6dfk76')
//        // cdt and cdn are useful for identifying which row triggered this event
//        console.log("Form Level of course", frm['doc']['level'], frm['doc']['enrolled_students'])
//    }
//});



//frappe.ui.form.on('Enrolled Students', {
//    // cdt is Child DocType name i.e Quotation Item
//    // cdn is the row name for e.g bbfcb8da6a
//    item_code(frm, cdt, cdn) {
//        let row = frappe.get_doc(cdt, cdn);
//        console.log("trow", row)
//    }
//})