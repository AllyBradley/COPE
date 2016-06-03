# Changelog

This is a list of changes made to the website and application for each release.

## v0.6.0 (TBC - Early May 2016) - The Follow Up edition
* Follow Up forms added for Initial, 3 Month, 6 Month, and 1 Year data collection (Issue #79)
* Health Economics forms added for Quality of Life data collection

## v0.5.1 (1 May 2016) - Bugfix 
* Internal documentation comments were appearing in the UI. These have been modifed or hidden (Issue #89)
* Online randomisation was failing, due to an incorrect validation check on an internal sequence number. (Issue #88)
* Question RE22 on the recipient form (Tape over regulator broken?) has not been saving. Incorrect field definition has been fixed. (Issue #81)

## v0.5.0 (29 Apr 2016) - Adversely Related
### New Features
* Adverse Event reporting added (Issue #80)
* Offline Randomisation Listings for Administrators. Shows available randomisation codes.
* Version Control implemented. All changes to site data are now preserved for audit and security purposes. (Issue #19)
* Changelog, and online User Manual added to the website (Issues #36 and #31)
* Transplantation Form now shows a checklist of eligibility criteria (Issue #42)
* Transplantation Form validation is now implemented using an expanded list of criteria as requested (Issue #45)

### Main changes
* Procurement form: 
 * Record information about cases that are not randomised (Issue #23)
 * Recipient randomisation display updating fixed (Issue #33)
* Transplantation form:
 * Changed the start process to require confirmation of allocation (Issue #44)
 * Added process to close form if allocation set to a non-trial location (Issue #41)
 * Ineligible cases are now shown a warning message to confirm answers, before closing the case on the subsequent save and confirm
 * General notes field added on form closing (Issue #46)
 * List of closed cases added for Administrators
* Expanded list of countries to include all of Europe (Locations app), rather than just the trial countries (Issue #25)
* Follow Up forms:
 * Urine Creatinine has been removed (Issue #49)
 * "Are they dead" question added to each stage of the forms (Issue #40)
* Security improvments made with:
 * Password rules implemented
 * Access controls tightened on all areas
 * Templates and menus now only show links for accessible (to you) areas
* Site navigation improved with: 
 * Breadcrumbs for all areas
 * Missing pages created for sections
 * Menu links updated
* Server emails have been enabled, allowing password reset requests to be done by all users, and sets up the option for having automated alerts in the future

### Minor (and background) changes
* Person's weight now recorded as a float, rather than an int (Issue #22)
* Fixed a middleware issue that caused problems with the debug language setting on the Test server (Issue #54)
* Help text added to the Is transplantable question (Issue #30)
* Fixed a bug which stopped hospitals with an apostrophe in their name from being selected (Issue #55)
* Date of Death is now back as a necessary OrganPerson attribute; This had implications for various date calculation methods, and save methods (such as saving when Donor death diagnosed is set). This was prompted again by Issue #40
* Age vs DoB validation message now shows the range of valid options to the user on error
* Template change to display version number from package details rather than hardcoded
* StaffPerson and FollowUp apps now use the common VersionControlModel class as their base
* Admin forms updated for new models and changes
* Improved the configuration setup to allow for easier deployment to multiple environments (location.env)
* Fixed a server error related to configuration for deployment on test server (wsgi.py)
* Split the compare:forms into their own package due to size growth
* Updated the core VersionControlModel class to handle saving for inherited classes
* New managers added to the Organ class to handle common queries
* Added `not_allocated_reason` to replace the redundant `allocated` attribute
* Two permission checking utilities added to determine if member of a list of groups, or has a specifed Job
* Many models updated to replace method calls with more appropriate property flags, and subsequent related corrections
* Organ now has an `explain_is_allocated` method that attempts to work out the allocated status of itself, and put it into words
* Foreign Key Widget now shows error messages when appropriate (previously they were not displayed)
* Developer documentation updated and expanded
* Repeated updates of third party libraries incorporated
 * Major version change to AutocompleteLight library (2 to 3) meant various changes, and several improvements to the functionality and appearance of type ahead select fields
* Server patching and updating done frequently

## v0.4.6 (2 Mar 2016) - Bugfix
* Changes made to allow use of local timezones in the website rather than just UST/GMT (Issue #34)
* Validation rules for calculating DoB corrected (Issue #35)

## v0.4.5 (18 Jan 2016) - Initial release
* First production release of the database, with focus on Procurement, Samples, Transplant, Locations, People, and related.
* User Documentation created (User Manual) and distributed by PDF
* Basic validation in place for the two forms
