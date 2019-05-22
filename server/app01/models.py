# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tblallocate(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    expertid = models.ForeignKey('Tbluserinfo', models.DO_NOTHING, db_column='ExpertID')  # Field name made lowercase.
    registergroupid = models.BigIntegerField(db_column='RegisterGroupID')  # Field name made lowercase.
    allocatedate = models.DateTimeField(db_column='AllocateDate')  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.
    score = models.IntegerField(db_column='Score')  # Field name made lowercase.
    arrangescore = models.FloatField(db_column='ArrangeScore')  # Field name made lowercase.
    evaluation = models.TextField(db_column='Evaluation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAllocate'


class Tblauthorcontesttyperelation(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    authorid = models.BigIntegerField(db_column='AuthorID')  # Field name made lowercase.
    contesttypeid = models.BigIntegerField(db_column='ContestTypeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAuthorContestTypeRelation'


class Tblauthorizationinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAuthorizationInfo'


class Tblchannelauthorrelation(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    authorid = models.ForeignKey(Tblauthorizationinfo, models.DO_NOTHING, db_column='AuthorID')  # Field name made lowercase.
    channelid = models.ForeignKey('Tblchanneltype', models.DO_NOTHING, db_column='ChannelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChannelAuthorRelation'


class Tblchannelcontent(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    channelcname = models.TextField(db_column='ChannelCName', blank=True, null=True)  # Field name made lowercase.
    channelctext = models.TextField(db_column='ChannelCText', blank=True, null=True)  # Field name made lowercase.
    channelctime = models.DateTimeField(db_column='ChannelCTime')  # Field name made lowercase.
    channelccomefrom = models.TextField(db_column='ChannelCComeFrom', blank=True, null=True)  # Field name made lowercase.
    channelcaudio = models.TextField(db_column='ChannelCAudio', blank=True, null=True)  # Field name made lowercase.
    channelcvedio = models.TextField(db_column='ChannelCVedio', blank=True, null=True)  # Field name made lowercase.
    channelctemplete = models.TextField(db_column='ChannelCTemplete', blank=True, null=True)  # Field name made lowercase.
    channelcpop = models.BooleanField(db_column='ChannelCPop')  # Field name made lowercase.
    channelctop = models.BooleanField(db_column='ChannelCTop')  # Field name made lowercase.
    channelcverify = models.BooleanField(db_column='ChannelCVerify')  # Field name made lowercase.
    channelcdefaultfont = models.BooleanField(db_column='ChannelCDefaultFont')  # Field name made lowercase.
    channeltypeid = models.ForeignKey('Tblchanneltype', models.DO_NOTHING, db_column='ChannelTypeID', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Tbluserinfo', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    hittime = models.IntegerField(db_column='HitTime')  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.
    oldid = models.CharField(db_column='OldID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChannelContent'


class Tblchannelcontentdoc(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    relationid = models.ForeignKey(Tblchannelcontent, models.DO_NOTHING, db_column='RelationID')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChannelContentDoc'


class Tblchannelcontentpic(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    relationid = models.ForeignKey(Tblchannelcontent, models.DO_NOTHING, db_column='RelationID')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChannelContentPic'


class Tblchanneltype(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parentindex = models.BigIntegerField(db_column='ParentIndex')  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.
    thelevel = models.SmallIntegerField(db_column='TheLevel')  # Field name made lowercase.
    childnum = models.IntegerField(db_column='ChildNum')  # Field name made lowercase.
    isleaf = models.BooleanField(db_column='IsLeaf')  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChannelType'


class Tblcommunicateinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    communicateipagenum = models.IntegerField(db_column='CommunicateIPageNum')  # Field name made lowercase.
    founddate = models.DateTimeField(db_column='FoundDate')  # Field name made lowercase.
    parentid = models.BigIntegerField(db_column='ParentID')  # Field name made lowercase.
    score = models.SmallIntegerField()
    status = models.BooleanField()
    studentid = models.ForeignKey('Tbluserinfo', models.DO_NOTHING, db_column='StudentID')  # Field name made lowercase.
    chapterid = models.ForeignKey('Tblcourseinfo', models.DO_NOTHING, db_column='ChapterID')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.
    selstudentid = models.ForeignKey('Tblstudentselcourserelation', models.DO_NOTHING, db_column='SelStudentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCommunicateInfo'


class Tblcontestflowadvice(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    typeid = models.BigIntegerField(db_column='TypeID')  # Field name made lowercase.
    flowid = models.BigIntegerField(db_column='FlowID')  # Field name made lowercase.
    starttime = models.CharField(db_column='StartTime', max_length=50)  # Field name made lowercase.
    endtime = models.CharField(db_column='EndTime', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblContestFlowAdvice'


class Tblcontestflowdetail(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    flowtypeid = models.ForeignKey('Tblcontestflowtype', models.DO_NOTHING, db_column='FlowTypeID')  # Field name made lowercase.
    contestinfoid = models.ForeignKey('Tblcontestinfo', models.DO_NOTHING, db_column='ContestInfoID')  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    weights = models.SmallIntegerField(db_column='Weights')  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    expertnumber = models.SmallIntegerField(db_column='ExpertNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblContestFlowDetail'


class Tblcontestflowtype(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblContestFlowType'


class Tblcontestinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    typeid = models.ForeignKey('Tblcontesttype', models.DO_NOTHING, db_column='TypeID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    creatorid = models.ForeignKey('Tbluserinfo', models.DO_NOTHING, db_column='CreatorID')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.
    isaudit = models.BooleanField(db_column='IsAudit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblContestInfo'


class Tblcontesttype(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.
    parentindex = models.BigIntegerField(db_column='ParentIndex')  # Field name made lowercase.
    thelevel = models.SmallIntegerField(db_column='TheLevel')  # Field name made lowercase.
    childnum = models.IntegerField(db_column='ChildNum')  # Field name made lowercase.
    isleaf = models.BooleanField(db_column='IsLeaf')  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    minteachernumber = models.SmallIntegerField(db_column='MinTeacherNumber')  # Field name made lowercase.
    maxteachernumber = models.SmallIntegerField(db_column='MaxTeacherNumber')  # Field name made lowercase.
    minteamernumber = models.SmallIntegerField(db_column='MinTeamerNumber')  # Field name made lowercase.
    maxteamernumber = models.SmallIntegerField(db_column='MaxTeamerNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblContestType'


class Tblcoursefileinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    openflag = models.BooleanField(db_column='OpenFlag')  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.
    relationid = models.ForeignKey('Tblcourseinfo', models.DO_NOTHING, db_column='RelationID')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCourseFileInfo'


class Tblcourseinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parentindex = models.BigIntegerField(db_column='ParentIndex')  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.
    thelevel = models.SmallIntegerField(db_column='TheLevel')  # Field name made lowercase.
    childnum = models.IntegerField(db_column='ChildNum')  # Field name made lowercase.
    isleaf = models.BooleanField(db_column='IsLeaf')  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCourseInfo'


class Tblcourseperiodrelation(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    periodid = models.ForeignKey('Tblperiodinfo', models.DO_NOTHING, db_column='PeriodID', blank=True, null=True)  # Field name made lowercase.
    courseid = models.ForeignKey(Tblcourseinfo, models.DO_NOTHING, db_column='CourseID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCoursePeriodRelation'


class Tbldepartmentinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    departmentiadd = models.TextField(db_column='DepartmentIADD', blank=True, null=True)  # Field name made lowercase.
    departmentipostalcode = models.TextField(db_column='DepartmentIPostalCode', blank=True, null=True)  # Field name made lowercase.
    departmentiphone = models.TextField(db_column='DepartmentIPhone', blank=True, null=True)  # Field name made lowercase.
    departmentifax = models.TextField(db_column='DepartmentIFax', blank=True, null=True)  # Field name made lowercase.
    departmentiemail = models.TextField(db_column='DepartmentIeMail', blank=True, null=True)  # Field name made lowercase.
    parentindex = models.BigIntegerField(db_column='ParentIndex')  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.
    thelevel = models.SmallIntegerField(db_column='TheLevel')  # Field name made lowercase.
    childnum = models.IntegerField(db_column='ChildNum')  # Field name made lowercase.
    isleaf = models.BooleanField(db_column='IsLeaf')  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDepartmentInfo'


class Tbldutyinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDutyInfo'


class Tblemailcontentinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    emailtitle = models.TextField(db_column='EmailTitle')  # Field name made lowercase.
    emailcontent = models.TextField(db_column='EmailContent')  # Field name made lowercase.
    code = models.TextField(db_column='Code')  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblEmailContentInfo'


class Tblexpertofflinerelation(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    offlineallocateid = models.BigIntegerField(db_column='OfflineAllocateID')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='UserID')  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExpertOfflineRelation'


class Tblgroupworkinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    relationid = models.ForeignKey('Tblregistergroup', models.DO_NOTHING, db_column='RelationID')  # Field name made lowercase.
    contestflowdetailid = models.ForeignKey(Tblcontestflowdetail, models.DO_NOTHING, db_column='ContestFlowDetailId')  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    founddate = models.DateTimeField(db_column='FoundDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGroupWorkInfo'


class Tblguestbook(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    guestbname = models.TextField(db_column='GuestBName', blank=True, null=True)  # Field name made lowercase.
    guestbhead = models.TextField(db_column='GuestBHead', blank=True, null=True)  # Field name made lowercase.
    guestbtext = models.TextField(db_column='GuestBText', blank=True, null=True)  # Field name made lowercase.
    guestbanswerflag = models.BooleanField(db_column='GuestBAnswerFlag')  # Field name made lowercase.
    guestbanswer = models.TextField(db_column='GuestBAnswer', blank=True, null=True)  # Field name made lowercase.
    guestbtime = models.DateTimeField(db_column='GuestBTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGuestBook'


class Tblluckinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    departmentname = models.TextField(db_column='DepartmentName', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    phonenumber = models.TextField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    lucknumber = models.BigIntegerField(db_column='LuckNumber')  # Field name made lowercase.
    isinevitable = models.BooleanField(db_column='IsInevitable')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLuckInfo'


class Tblmaininfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    maininame = models.TextField(db_column='MainIName', blank=True, null=True)  # Field name made lowercase.
    mainiurl = models.TextField(db_column='MainIURL', blank=True, null=True)  # Field name made lowercase.
    mainiemail = models.TextField(db_column='MainIEmail', blank=True, null=True)  # Field name made lowercase.
    mainiemailpass = models.TextField(db_column='MainIEmailPass', blank=True, null=True)  # Field name made lowercase.
    mainiemailemailsmtp = models.TextField(db_column='MainIEmailEmailSmtp', blank=True, null=True)  # Field name made lowercase.
    mainikeywords = models.TextField(db_column='MainIKeyWords', blank=True, null=True)  # Field name made lowercase.
    mainifootmark = models.TextField(db_column='MainIFootMark', blank=True, null=True)  # Field name made lowercase.
    mainivisitednum = models.IntegerField(db_column='MainIVisitedNum')  # Field name made lowercase.
    mainivisitedvisiable = models.BooleanField(db_column='MainIVisitedVisiable')  # Field name made lowercase.
    mainiinformation = models.TextField(db_column='MainIInformation', blank=True, null=True)  # Field name made lowercase.
    mainiaboutus = models.TextField(db_column='MainIAboutUS', blank=True, null=True)  # Field name made lowercase.
    allnum = models.IntegerField(db_column='AllNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMainInfo'


class Tblmarkinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    markigetnum = models.SmallIntegerField(db_column='MarkIGetNum')  # Field name made lowercase.
    markidate = models.DateTimeField(db_column='MarkIDate', blank=True, null=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Tbluserinfo', models.DO_NOTHING, db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
    testquestionid = models.ForeignKey('Tbltestquestion', models.DO_NOTHING, db_column='TestQuestionID', blank=True, null=True)  # Field name made lowercase.
    periodid = models.ForeignKey('Tblperiodinfo', models.DO_NOTHING, db_column='PeriodID', blank=True, null=True)  # Field name made lowercase.
    selstudentid = models.ForeignKey('Tblstudentselcourserelation', models.DO_NOTHING, db_column='SelStudentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMarkInfo'


class Tblofflineallocateinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    contestinfoid = models.BigIntegerField(db_column='ContestInfoID')  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOfflineAllocateInfo'


class Tblofflinescoremaininfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    groupid = models.BigIntegerField(db_column='GroupID')  # Field name made lowercase.
    expertid = models.BigIntegerField(db_column='ExpertID')  # Field name made lowercase.
    typeid = models.BigIntegerField(db_column='TypeID')  # Field name made lowercase.
    score = models.IntegerField(db_column='Score')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOfflineScoreMainInfo'


class Tbloperationauthorrelation(models.Model):
    authorid = models.ForeignKey(Tblauthorizationinfo, models.DO_NOTHING, db_column='AuthorID')  # Field name made lowercase.
    operationid = models.ForeignKey('Tbloperationinfo', models.DO_NOTHING, db_column='OperationID')  # Field name made lowercase.
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    searchflag = models.BooleanField(db_column='SearchFlag')  # Field name made lowercase.
    addflag = models.BooleanField(db_column='AddFlag')  # Field name made lowercase.
    editflag = models.BooleanField(db_column='EditFlag')  # Field name made lowercase.
    deleteflag = models.BooleanField(db_column='DeleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOperationAuthorRelation'


class Tbloperationinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parentindex = models.BigIntegerField(db_column='ParentIndex')  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.
    thelevel = models.SmallIntegerField(db_column='TheLevel')  # Field name made lowercase.
    childnum = models.IntegerField(db_column='ChildNum')  # Field name made lowercase.
    isleaf = models.BooleanField(db_column='IsLeaf')  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOperationInfo'


class Tblpaticalscore(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    allocateid = models.ForeignKey(Tblallocate, models.DO_NOTHING, db_column='AllocateID')  # Field name made lowercase.
    typeid = models.ForeignKey('Tblscoretypeinfo', models.DO_NOTHING, db_column='TypeID')  # Field name made lowercase.
    score = models.IntegerField(db_column='Score')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPaticalScore'


class Tblperiodinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPeriodInfo'


class Tblregistergroup(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    contestinfoid = models.ForeignKey(Tblcontestinfo, models.DO_NOTHING, db_column='ContestInfoID')  # Field name made lowercase.
    creatorid = models.ForeignKey('Tbluserinfo', models.DO_NOTHING, db_column='CreatorID')  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate')  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.
    schoolid = models.ForeignKey(Tbldepartmentinfo, models.DO_NOTHING, db_column='SchoolID')  # Field name made lowercase.
    groupnumber = models.CharField(db_column='GroupNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workname = models.CharField(db_column='WorkName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    groupresult = models.CharField(db_column='GroupResult', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contesttypeid = models.BigIntegerField(db_column='ContestTypeID')  # Field name made lowercase.
    verifyflag = models.BooleanField(db_column='VerifyFlag')  # Field name made lowercase.
    offlineallocateid = models.BigIntegerField(db_column='OfflineAllocateID', blank=True, null=True)  # Field name made lowercase.
    offlinescore = models.FloatField(db_column='OfflineScore')  # Field name made lowercase.
    offlinearrangescore = models.FloatField(db_column='OfflineArrangeScore')  # Field name made lowercase.
    allscore = models.FloatField(db_column='AllScore')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRegisterGroup'


class Tblregisteruser(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    registergroupid = models.ForeignKey(Tblregistergroup, models.DO_NOTHING, db_column='RegisterGroupID')  # Field name made lowercase.
    userid = models.ForeignKey('Tbluserinfo', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRegisterUser'


class Tblscoretypeadvice(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    theorder = models.SmallIntegerField(db_column='TheOrder')  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblScoreTypeAdvice'


class Tblscoretypeinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    contestflowdetailid = models.ForeignKey(Tblcontestflowdetail, models.DO_NOTHING, db_column='ContestFlowDetailID')  # Field name made lowercase.
    scorepercent = models.FloatField(db_column='ScorePercent')  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.
    scoretypeadviceid = models.BigIntegerField(db_column='ScoreTypeAdviceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblScoreTypeInfo'


class Tblstudentselcourserelation(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Tbluserinfo', models.DO_NOTHING, db_column='StudentID')  # Field name made lowercase.
    courseperiodid = models.ForeignKey(Tblcourseperiodrelation, models.DO_NOTHING, db_column='CoursePeriodID')  # Field name made lowercase.
    lastscore = models.FloatField(db_column='LastScore')  # Field name made lowercase.
    dutyscore = models.FloatField(db_column='DutyScore')  # Field name made lowercase.
    markscore = models.FloatField(db_column='MarkScore')  # Field name made lowercase.
    aftermarkscore = models.FloatField(db_column='AfterMarkScore')  # Field name made lowercase.
    communicationscore = models.FloatField(db_column='CommunicationScore')  # Field name made lowercase.
    testreportscore = models.FloatField(db_column='TestReportScore')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStudentSelCourseRelation'


class Tbltestquestion(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    question = models.TextField(db_column='Question', blank=True, null=True)  # Field name made lowercase.
    answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
    degree = models.SmallIntegerField(db_column='Degree')  # Field name made lowercase.
    chapterid = models.ForeignKey(Tblcourseinfo, models.DO_NOTHING, db_column='ChapterID', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTestQuestion'


class Tbluserauthorrelation(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    authorid = models.ForeignKey(Tblauthorizationinfo, models.DO_NOTHING, db_column='AuthorID')  # Field name made lowercase.
    userid = models.ForeignKey('Tbluserinfo', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUserAuthorRelation'


class Tbluserinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    usericode = models.TextField(db_column='UserICode', blank=True, null=True)  # Field name made lowercase.
    useripsd = models.TextField(db_column='UserIPsd', blank=True, null=True)  # Field name made lowercase.
    useriregisterdate = models.DateTimeField(db_column='UserIRegisterDate', blank=True, null=True)  # Field name made lowercase.
    userisex = models.CharField(db_column='UserISex', max_length=2, blank=True, null=True)  # Field name made lowercase.
    useriidcard = models.TextField(db_column='UserIIDCard', blank=True, null=True)  # Field name made lowercase.
    useribirth = models.DateTimeField(db_column='UserIBirth', blank=True, null=True)  # Field name made lowercase.
    useriaddress = models.TextField(db_column='UserIAddress', blank=True, null=True)  # Field name made lowercase.
    useripostalcode = models.TextField(db_column='UserIPostalCode', blank=True, null=True)  # Field name made lowercase.
    useristudentnumber = models.TextField(db_column='UserIStudentNumber', blank=True, null=True)  # Field name made lowercase.
    userimobilephone = models.TextField(db_column='UserIMobilePhone', blank=True, null=True)  # Field name made lowercase.
    useriemail = models.TextField(db_column='UserIeMail', blank=True, null=True)  # Field name made lowercase.
    useridutyiid = models.ForeignKey(Tbldutyinfo, models.DO_NOTHING, db_column='UserIDutyIID', blank=True, null=True)  # Field name made lowercase.
    useridepartmentiid = models.ForeignKey(Tbldepartmentinfo, models.DO_NOTHING, db_column='UserIDepartmentIID', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    delflag = models.BooleanField(db_column='DelFlag')  # Field name made lowercase.
    verifyflag = models.BooleanField(db_column='VerifyFlag')  # Field name made lowercase.
    wholedepartmentname = models.TextField(db_column='WholeDepartmentName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUserInfo'


class TblahjsjjyAttachment(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    module = models.TextField()
    catid = models.BigIntegerField()
    filename = models.TextField()
    filepath = models.TextField()
    filesize = models.BigIntegerField()
    fileext = models.TextField()
    isimage = models.BigIntegerField()
    isthumb = models.BigIntegerField()
    userid = models.BigIntegerField()
    isadmin = models.BigIntegerField()
    uploadtime = models.BigIntegerField()
    uploadip = models.TextField()
    status = models.BigIntegerField()
    authcode = models.TextField()

    class Meta:
        managed = False
        db_table = 'tblahjsjjy_attachment'


class TblahjsjjyAttachmentindex(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    keyid = models.TextField()
    aid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tblahjsjjy_attachmentindex'


class TblahjsjjyContent(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    catid = models.BigIntegerField()
    typeid = models.BigIntegerField()
    title = models.TextField()
    style = models.TextField()
    thumb = models.TextField()
    keywords = models.TextField()
    tags = models.TextField()
    description = models.TextField()
    posid = models.BigIntegerField()
    url = models.TextField()
    listorder = models.BigIntegerField()
    status = models.BigIntegerField()
    sysadd = models.BigIntegerField()
    islink = models.BigIntegerField()
    username = models.TextField()
    inputtime = models.BigIntegerField()
    updatetime = models.BigIntegerField()
    views = models.BigIntegerField()
    yesterdayviews = models.BigIntegerField()
    dayviews = models.BigIntegerField()
    weekviews = models.BigIntegerField()
    monthviews = models.BigIntegerField()
    viewsupdatetime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tblahjsjjy_content'


class TblahjsjjyContentdata(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    scontent = models.TextField(db_column='sContent')  # Field name made lowercase.
    paginationtype = models.BigIntegerField()
    maxcharperpage = models.BigIntegerField()
    template = models.CharField(max_length=50)
    paytype = models.BigIntegerField()
    allow_comment = models.BigIntegerField()
    relation = models.TextField()

    class Meta:
        managed = False
        db_table = 'tblahjsjjy_contentdata'
