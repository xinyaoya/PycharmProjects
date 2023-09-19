<template>
    <Tabs value="myUI" type="card">
        <TabPane label="大话西游" name="name1">
            <div class="container">
                <Row align="middle">
                    用户名：
                    <Input v-model="username" placeholder="请输入用户名"
                    style="width: 200px" />
                </Row>
                <Row align="middle">
                    输入数字：
                    <InputNumber :max="100" :min="0" v-model="number" />
                </Row>
                <Row>
                    单选：
                    <RadioGroup v-model="phone">
                        <Radio label="apple">
                            <Icon type="logo-apple"></Icon>
                            <span>Apple</span>
                        </Radio>
                        <Radio label="android">
                            <Icon type="logo-android"></Icon>
                            <span>Android</span>
                        </Radio>
                        <Radio label="windows">
                            <Icon type="logo-windows"></Icon>
                            <span>Windows</span>
                        </Radio>
                    </RadioGroup>
                </Row>
                <Row>
                    多选：
                    <CheckboxGroup v-model="fruit">
                        <Checkbox label="香蕉"></Checkbox>
                        <Checkbox label="苹果"></Checkbox>
                        <Checkbox label="西瓜"></Checkbox>
                    </CheckboxGroup>
                </Row>
                <Row>
                    开关：
                    <Switch v-model="switch_value" />
                </Row>
                <Row align="middle">
                    下拉框：
                    <Select v-model="dropdown" style="width:200px">
                        <Option v-for="item in dropdownList" :value="item.value"
                        :key="item.value">{{ item.label }}
                        </Option>
                    </Select>
                </Row>
                <Row align="middle">
                    滑块：
                    <Card style="width: 240px;">
                        <Slider v-model="slider_value"></Slider>
                    </Card>
                </Row>
                <Row align="middle">
                    日期：
                    <DatePicker :model-value="date" type="date" placeholder="Select date"
                    style="width: 200px"
                        @on-change="dateClick" />
                </Row>
                <Row align="middle">
                    时间：
                    <TimePicker :model-value="time" format="HH:mm:ss" placeholder="Select time"
                    style="width: 168px"
                        @on-change="timeClick" />
                </Row>
                <Row align="middle">
                    打分：
                    <Rate allow-half v-model="rate" />
                    <span style="color: #f5a623">{{ rate }}</span>
                </Row>
                <Row align="middle">
                    颜色：
                    <ColorPicker v-model="color" transfer=true />
                </Row>
            </div>
        </TabPane>
        <TabPane label="二话西游" name="name2">
            <div class="container">
                <Row align="middle">
                    密码：
                    <Input v-model="password" placeholder="请输入密码" style="width: 200px"/>
                </Row>
            </div>
        </TabPane>
        <TabPane label="三打白骨精" name="name3">
            <div class="container">
                <Row align="middle">
                    个性签名：
                    <Input v-model="profile" placeholder="" style="width: 200px" />
                </Row>
            </div>
        </TabPane>
    </Tabs>
</template>

<script>
import 'view-ui-plus/dist/styles/viewuiplus.css'
import moment from 'moment';
import xp from 'xiaopy_js'

export default {
    name: "Xiaopy",
    props: {
        msg: String
    },
    data() {
        return {
            username: xp.stringValue("username") || "",
            phone: xp.stringValue("phone") || "apple",
            fruit: xp.stringValue("fruit") ? xp.stringValue("fruit").split(",")
            : ["香蕉", "苹果"],
            switch_value: xp.boolValue("switch_value") || false,
            dropdownList: [
                {
                    value: "New York",
                    label: "纽约"
                },
                {
                    value: "Lodon",
                    label: "伦敦"
                }
            ],
            dropdown: xp.stringValue("dropdown") || "",
            slider_value: xp.intValue("slider_value") || 10,
            date: new Date(xp.stringValue("date")) || new Date(),
            time: xp.stringValue("time") || "12:00:00",
            number: xp.intValue("number") || 3,
            rate: xp.floatValue("rate") || 2.5,
            color: xp.stringValue("color") || '#3475BA',
            password: xp.stringValue("password") || '',
            profile: xp.stringValue("profile") || ''
        };
    },
    methods: {
        dateClick(date) {
            this.date = date
        },
        timeClick(time) {
            this.time = time
        }
    },
    mounted() {
        const self = this
        xp.onDataChange(function (group, key, value) {
            console.log("xiaopy ui", group, key, value)
            if (key === "username") {
                self.username = value
            } else if (key === "phone") {
                self.phone = value
            } else if (key === "fruit") {
                self.fruit = value.split(",")
            } else if (key === "switch_value") {
                self.switch_value = value
            } else if (key === "dropdown") {
                self.dropdown = value
            } else if (key === "slider_value") {
                self.slider_value = value
            } else if (key === "date") {
                self.date = new Date(value)
            } else if (key === "time") {
                self.time = value
            } else if (key === "number") {
                self.number = value
            } else if (key === "rate") {
                self.rate = value
            } else if (key === "color") {
                self.color = value
            } else if (key === "password") {
                self.password = value
            } else if (key === "profile") {
                self.profile = value
            }
        })

        xp.saveData(function () {
            xp.setStringValue("username", self.username)
            xp.setStringValue("phone", self.phone)
            xp.setStringValue("fruit", self.fruit.join(","))
            xp.setStringValue("dropdown", self.dropdown);
            xp.setIntValue("slider_value", self.slider_value)
            xp.setStringValue("date", moment(self.date).format("YYYY-MM-DD"))
            xp.setStringValue("time", self.time);
            xp.setIntValue("number", self.number)
            xp.setFloatValue("rate", self.rate)
            xp.setStringValue("color", self.color)
            xp.setBoolValue("switch_value", self.switch_value)
            xp.setStringValue("password", self.password)
            xp.setStringValue("profile", self.profile)
        })
    },
}
</script>

<style scoped>
.container {
    width: 100%;
    height: 100%;
    padding-inline: 15px;
}

.ivu-row {
    margin-top: 10px;
}
</style>