# Generated by Django 2.1.8 on 2019-05-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblahjsjjyAttachment',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('module', models.TextField()),
                ('catid', models.BigIntegerField()),
                ('filename', models.TextField()),
                ('filepath', models.TextField()),
                ('filesize', models.BigIntegerField()),
                ('fileext', models.TextField()),
                ('isimage', models.BigIntegerField()),
                ('isthumb', models.BigIntegerField()),
                ('userid', models.BigIntegerField()),
                ('isadmin', models.BigIntegerField()),
                ('uploadtime', models.BigIntegerField()),
                ('uploadip', models.TextField()),
                ('status', models.BigIntegerField()),
                ('authcode', models.TextField()),
            ],
            options={
                'db_table': 'tblahjsjjy_attachment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblahjsjjyAttachmentindex',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('keyid', models.TextField()),
                ('aid', models.BigIntegerField()),
            ],
            options={
                'db_table': 'tblahjsjjy_attachmentindex',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblahjsjjyContent',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('catid', models.BigIntegerField()),
                ('typeid', models.BigIntegerField()),
                ('title', models.TextField()),
                ('style', models.TextField()),
                ('thumb', models.TextField()),
                ('keywords', models.TextField()),
                ('tags', models.TextField()),
                ('description', models.TextField()),
                ('posid', models.BigIntegerField()),
                ('url', models.TextField()),
                ('listorder', models.BigIntegerField()),
                ('status', models.BigIntegerField()),
                ('sysadd', models.BigIntegerField()),
                ('islink', models.BigIntegerField()),
                ('username', models.TextField()),
                ('inputtime', models.BigIntegerField()),
                ('updatetime', models.BigIntegerField()),
                ('views', models.BigIntegerField()),
                ('yesterdayviews', models.BigIntegerField()),
                ('dayviews', models.BigIntegerField()),
                ('weekviews', models.BigIntegerField()),
                ('monthviews', models.BigIntegerField()),
                ('viewsupdatetime', models.BigIntegerField()),
            ],
            options={
                'db_table': 'tblahjsjjy_content',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblahjsjjyContentdata',
            fields=[
                ('id', models.BigIntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('scontent', models.TextField(db_column='sContent')),
                ('paginationtype', models.BigIntegerField()),
                ('maxcharperpage', models.BigIntegerField()),
                ('template', models.CharField(max_length=50)),
                ('paytype', models.BigIntegerField()),
                ('allow_comment', models.BigIntegerField()),
                ('relation', models.TextField()),
            ],
            options={
                'db_table': 'tblahjsjjy_contentdata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblallocate',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('registergroupid', models.BigIntegerField(db_column='RegisterGroupID')),
                ('allocatedate', models.DateTimeField(db_column='AllocateDate')),
                ('delflag', models.BooleanField(db_column='DelFlag')),
                ('score', models.IntegerField(db_column='Score')),
                ('arrangescore', models.FloatField(db_column='ArrangeScore')),
                ('evaluation', models.TextField(blank=True, db_column='Evaluation', null=True)),
            ],
            options={
                'db_table': 'tblAllocate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblauthorcontesttyperelation',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('authorid', models.BigIntegerField(db_column='AuthorID')),
                ('contesttypeid', models.BigIntegerField(db_column='ContestTypeID')),
            ],
            options={
                'db_table': 'tblAuthorContestTypeRelation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblauthorizationinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblAuthorizationInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblchannelauthorrelation',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tblChannelAuthorRelation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblchannelcontent',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('channelcname', models.TextField(blank=True, db_column='ChannelCName', null=True)),
                ('channelctext', models.TextField(blank=True, db_column='ChannelCText', null=True)),
                ('channelctime', models.DateTimeField(db_column='ChannelCTime')),
                ('channelccomefrom', models.TextField(blank=True, db_column='ChannelCComeFrom', null=True)),
                ('channelcaudio', models.TextField(blank=True, db_column='ChannelCAudio', null=True)),
                ('channelcvedio', models.TextField(blank=True, db_column='ChannelCVedio', null=True)),
                ('channelctemplete', models.TextField(blank=True, db_column='ChannelCTemplete', null=True)),
                ('channelcpop', models.BooleanField(db_column='ChannelCPop')),
                ('channelctop', models.BooleanField(db_column='ChannelCTop')),
                ('channelcverify', models.BooleanField(db_column='ChannelCVerify')),
                ('channelcdefaultfont', models.BooleanField(db_column='ChannelCDefaultFont')),
                ('hittime', models.IntegerField(db_column='HitTime')),
                ('delflag', models.BooleanField(db_column='DelFlag')),
                ('oldid', models.CharField(blank=True, db_column='OldID', max_length=50, null=True)),
            ],
            options={
                'db_table': 'tblChannelContent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblchannelcontentdoc',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('address', models.TextField(blank=True, db_column='Address', null=True)),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
            ],
            options={
                'db_table': 'tblChannelContentDoc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblchannelcontentpic',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('address', models.TextField(blank=True, db_column='Address', null=True)),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
            ],
            options={
                'db_table': 'tblChannelContentPic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblchanneltype',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('parentindex', models.BigIntegerField(db_column='ParentIndex')),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
                ('thelevel', models.SmallIntegerField(db_column='TheLevel')),
                ('childnum', models.IntegerField(db_column='ChildNum')),
                ('isleaf', models.BooleanField(db_column='IsLeaf')),
                ('code', models.TextField(blank=True, db_column='Code', null=True)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblChannelType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblcommunicateinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('communicateipagenum', models.IntegerField(db_column='CommunicateIPageNum')),
                ('founddate', models.DateTimeField(db_column='FoundDate')),
                ('parentid', models.BigIntegerField(db_column='ParentID')),
                ('score', models.SmallIntegerField()),
                ('status', models.BooleanField()),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblCommunicateInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblcontestflowadvice',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('typeid', models.BigIntegerField(db_column='TypeID')),
                ('flowid', models.BigIntegerField(db_column='FlowID')),
                ('starttime', models.CharField(db_column='StartTime', max_length=50)),
                ('endtime', models.CharField(db_column='EndTime', max_length=50)),
            ],
            options={
                'db_table': 'tblContestFlowAdvice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblcontestflowdetail',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('startdate', models.DateField(blank=True, db_column='StartDate', null=True)),
                ('enddate', models.DateField(blank=True, db_column='EndDate', null=True)),
                ('weights', models.SmallIntegerField(db_column='Weights')),
                ('delflag', models.BooleanField(db_column='DelFlag')),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('expertnumber', models.SmallIntegerField(db_column='ExpertNumber')),
            ],
            options={
                'db_table': 'tblContestFlowDetail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblcontestflowtype',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('delflag', models.BooleanField(db_column='DelFlag')),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
            ],
            options={
                'db_table': 'tblContestFlowType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblcontestinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('delflag', models.BooleanField(db_column='DelFlag')),
                ('isaudit', models.BooleanField(db_column='IsAudit')),
            ],
            options={
                'db_table': 'tblContestInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblcontesttype',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('delflag', models.BooleanField(db_column='DelFlag')),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
                ('parentindex', models.BigIntegerField(db_column='ParentIndex')),
                ('thelevel', models.SmallIntegerField(db_column='TheLevel')),
                ('childnum', models.IntegerField(db_column='ChildNum')),
                ('isleaf', models.BooleanField(db_column='IsLeaf')),
                ('code', models.TextField(blank=True, db_column='Code', null=True)),
                ('minteachernumber', models.SmallIntegerField(db_column='MinTeacherNumber')),
                ('maxteachernumber', models.SmallIntegerField(db_column='MaxTeacherNumber')),
                ('minteamernumber', models.SmallIntegerField(db_column='MinTeamerNumber')),
                ('maxteamernumber', models.SmallIntegerField(db_column='MaxTeamerNumber')),
            ],
            options={
                'db_table': 'tblContestType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblcoursefileinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('openflag', models.BooleanField(db_column='OpenFlag')),
                ('delflag', models.BooleanField(db_column='DelFlag')),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('address', models.TextField(blank=True, db_column='Address', null=True)),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
            ],
            options={
                'db_table': 'tblCourseFileInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblcourseinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('parentindex', models.BigIntegerField(db_column='ParentIndex')),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
                ('thelevel', models.SmallIntegerField(db_column='TheLevel')),
                ('childnum', models.IntegerField(db_column='ChildNum')),
                ('isleaf', models.BooleanField(db_column='IsLeaf')),
                ('code', models.TextField(blank=True, db_column='Code', null=True)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblCourseInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblcourseperiodrelation',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tblCoursePeriodRelation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbldepartmentinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('departmentiadd', models.TextField(blank=True, db_column='DepartmentIADD', null=True)),
                ('departmentipostalcode', models.TextField(blank=True, db_column='DepartmentIPostalCode', null=True)),
                ('departmentiphone', models.TextField(blank=True, db_column='DepartmentIPhone', null=True)),
                ('departmentifax', models.TextField(blank=True, db_column='DepartmentIFax', null=True)),
                ('departmentiemail', models.TextField(blank=True, db_column='DepartmentIeMail', null=True)),
                ('parentindex', models.BigIntegerField(db_column='ParentIndex')),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
                ('thelevel', models.SmallIntegerField(db_column='TheLevel')),
                ('childnum', models.IntegerField(db_column='ChildNum')),
                ('isleaf', models.BooleanField(db_column='IsLeaf')),
                ('code', models.TextField(blank=True, db_column='Code', null=True)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblDepartmentInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbldutyinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblDutyInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblemailcontentinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('emailtitle', models.TextField(db_column='EmailTitle')),
                ('emailcontent', models.TextField(db_column='EmailContent')),
                ('code', models.TextField(db_column='Code')),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblEmailContentInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblexpertofflinerelation',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('offlineallocateid', models.BigIntegerField(db_column='OfflineAllocateID')),
                ('userid', models.BigIntegerField(db_column='UserID')),
                ('rolename', models.CharField(blank=True, db_column='RoleName', max_length=50, null=True)),
            ],
            options={
                'db_table': 'tblExpertOfflineRelation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblgroupworkinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=50, null=True)),
                ('founddate', models.DateTimeField(db_column='FoundDate')),
            ],
            options={
                'db_table': 'tblGroupWorkInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblguestbook',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('guestbname', models.TextField(blank=True, db_column='GuestBName', null=True)),
                ('guestbhead', models.TextField(blank=True, db_column='GuestBHead', null=True)),
                ('guestbtext', models.TextField(blank=True, db_column='GuestBText', null=True)),
                ('guestbanswerflag', models.BooleanField(db_column='GuestBAnswerFlag')),
                ('guestbanswer', models.TextField(blank=True, db_column='GuestBAnswer', null=True)),
                ('guestbtime', models.DateTimeField(db_column='GuestBTime')),
            ],
            options={
                'db_table': 'tblGuestBook',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblluckinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('departmentname', models.TextField(blank=True, db_column='DepartmentName', null=True)),
                ('name', models.TextField(db_column='Name')),
                ('phonenumber', models.TextField(blank=True, db_column='PhoneNumber', null=True)),
                ('lucknumber', models.BigIntegerField(db_column='LuckNumber')),
                ('isinevitable', models.BooleanField(db_column='IsInevitable')),
            ],
            options={
                'db_table': 'tblLuckInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblmaininfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('maininame', models.TextField(blank=True, db_column='MainIName', null=True)),
                ('mainiurl', models.TextField(blank=True, db_column='MainIURL', null=True)),
                ('mainiemail', models.TextField(blank=True, db_column='MainIEmail', null=True)),
                ('mainiemailpass', models.TextField(blank=True, db_column='MainIEmailPass', null=True)),
                ('mainiemailemailsmtp', models.TextField(blank=True, db_column='MainIEmailEmailSmtp', null=True)),
                ('mainikeywords', models.TextField(blank=True, db_column='MainIKeyWords', null=True)),
                ('mainifootmark', models.TextField(blank=True, db_column='MainIFootMark', null=True)),
                ('mainivisitednum', models.IntegerField(db_column='MainIVisitedNum')),
                ('mainivisitedvisiable', models.BooleanField(db_column='MainIVisitedVisiable')),
                ('mainiinformation', models.TextField(blank=True, db_column='MainIInformation', null=True)),
                ('mainiaboutus', models.TextField(blank=True, db_column='MainIAboutUS', null=True)),
                ('allnum', models.IntegerField(blank=True, db_column='AllNum', null=True)),
            ],
            options={
                'db_table': 'tblMainInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblmarkinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('markigetnum', models.SmallIntegerField(db_column='MarkIGetNum')),
                ('markidate', models.DateTimeField(blank=True, db_column='MarkIDate', null=True)),
            ],
            options={
                'db_table': 'tblMarkInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblofflineallocateinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('contestinfoid', models.BigIntegerField(db_column='ContestInfoID')),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblOfflineAllocateInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblofflinescoremaininfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('groupid', models.BigIntegerField(db_column='GroupID')),
                ('expertid', models.BigIntegerField(db_column='ExpertID')),
                ('typeid', models.BigIntegerField(db_column='TypeID')),
                ('score', models.IntegerField(db_column='Score')),
            ],
            options={
                'db_table': 'tblOfflineScoreMainInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbloperationauthorrelation',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('searchflag', models.BooleanField(db_column='SearchFlag')),
                ('addflag', models.BooleanField(db_column='AddFlag')),
                ('editflag', models.BooleanField(db_column='EditFlag')),
                ('deleteflag', models.BooleanField(db_column='DeleteFlag')),
            ],
            options={
                'db_table': 'tblOperationAuthorRelation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbloperationinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('parentindex', models.BigIntegerField(db_column='ParentIndex')),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
                ('thelevel', models.SmallIntegerField(db_column='TheLevel')),
                ('childnum', models.IntegerField(db_column='ChildNum')),
                ('isleaf', models.BooleanField(db_column='IsLeaf')),
                ('code', models.TextField(blank=True, db_column='Code', null=True)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblOperationInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblpaticalscore',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('score', models.IntegerField(db_column='Score')),
            ],
            options={
                'db_table': 'tblPaticalScore',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblperiodinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblPeriodInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblregistergroup',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('createdate', models.DateField(db_column='CreateDate')),
                ('delflag', models.BooleanField(db_column='DelFlag')),
                ('groupnumber', models.CharField(blank=True, db_column='GroupNumber', max_length=50, null=True)),
                ('groupname', models.CharField(blank=True, db_column='GroupName', max_length=50, null=True)),
                ('workname', models.CharField(blank=True, db_column='WorkName', max_length=50, null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('score', models.FloatField(blank=True, db_column='Score', null=True)),
                ('groupresult', models.CharField(blank=True, db_column='GroupResult', max_length=50, null=True)),
                ('contesttypeid', models.BigIntegerField(db_column='ContestTypeID')),
                ('verifyflag', models.BooleanField(db_column='VerifyFlag')),
                ('offlineallocateid', models.BigIntegerField(blank=True, db_column='OfflineAllocateID', null=True)),
                ('offlinescore', models.FloatField(db_column='OfflineScore')),
                ('offlinearrangescore', models.FloatField(db_column='OfflineArrangeScore')),
                ('allscore', models.FloatField(db_column='AllScore')),
            ],
            options={
                'db_table': 'tblRegisterGroup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblregisteruser',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('rolename', models.CharField(blank=True, db_column='RoleName', max_length=50, null=True)),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
            ],
            options={
                'db_table': 'tblRegisterUser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblscoretypeadvice',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('theorder', models.SmallIntegerField(db_column='TheOrder')),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblScoreTypeAdvice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblscoretypeinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('scorepercent', models.FloatField(db_column='ScorePercent')),
                ('delflag', models.BooleanField(db_column='DelFlag')),
                ('scoretypeadviceid', models.BigIntegerField(db_column='ScoreTypeAdviceID')),
            ],
            options={
                'db_table': 'tblScoreTypeInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblstudentselcourserelation',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('lastscore', models.FloatField(db_column='LastScore')),
                ('dutyscore', models.FloatField(db_column='DutyScore')),
                ('markscore', models.FloatField(db_column='MarkScore')),
                ('aftermarkscore', models.FloatField(db_column='AfterMarkScore')),
                ('communicationscore', models.FloatField(db_column='CommunicationScore')),
                ('testreportscore', models.FloatField(db_column='TestReportScore')),
            ],
            options={
                'db_table': 'tblStudentSelCourseRelation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbltestquestion',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('type', models.TextField(blank=True, db_column='Type', null=True)),
                ('question', models.TextField(blank=True, db_column='Question', null=True)),
                ('answer', models.TextField(blank=True, db_column='Answer', null=True)),
                ('degree', models.SmallIntegerField(db_column='Degree')),
                ('delflag', models.BooleanField(db_column='DelFlag')),
            ],
            options={
                'db_table': 'tblTestQuestion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbluserauthorrelation',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tblUserAuthorRelation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbluserinfo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('usericode', models.TextField(blank=True, db_column='UserICode', null=True)),
                ('useripsd', models.TextField(blank=True, db_column='UserIPsd', null=True)),
                ('useriregisterdate', models.DateTimeField(blank=True, db_column='UserIRegisterDate', null=True)),
                ('userisex', models.CharField(blank=True, db_column='UserISex', max_length=2, null=True)),
                ('useriidcard', models.TextField(blank=True, db_column='UserIIDCard', null=True)),
                ('useribirth', models.DateTimeField(blank=True, db_column='UserIBirth', null=True)),
                ('useriaddress', models.TextField(blank=True, db_column='UserIAddress', null=True)),
                ('useripostalcode', models.TextField(blank=True, db_column='UserIPostalCode', null=True)),
                ('useristudentnumber', models.TextField(blank=True, db_column='UserIStudentNumber', null=True)),
                ('userimobilephone', models.TextField(blank=True, db_column='UserIMobilePhone', null=True)),
                ('useriemail', models.TextField(blank=True, db_column='UserIeMail', null=True)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('delflag', models.BooleanField(db_column='DelFlag')),
                ('verifyflag', models.BooleanField(db_column='VerifyFlag')),
                ('wholedepartmentname', models.TextField(blank=True, db_column='WholeDepartmentName', null=True)),
            ],
            options={
                'db_table': 'tblUserInfo',
                'managed': False,
            },
        ),
    ]