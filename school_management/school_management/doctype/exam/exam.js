// Copyright (c) 2022, Advintic and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Exam", {
 	refresh(frm) {
         frm.add_custom_button(__('Email Students'), function(){
          if(frm.doc.course && frm.doc.appointment){
             frappe.call({
                method: "school_management.school_management.doctype.exam.exam.send_mail", //dotted path to server method
                args: {'course': frm.doc.course, 'appointment': frm.doc.appointment},
                callback: function(r) {
                    // code snippet
                }
            });
          }else{
                frappe.msgprint("Can't send Emails without submitting course and appointment time!");
          }

    })
 	},
 });

